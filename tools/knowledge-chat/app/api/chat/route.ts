import { streamText, tool, convertToCoreMessages } from 'ai';
import { z } from 'zod';
import { openai, createOpenAI } from '@ai-sdk/openai';
import { anthropic } from '@ai-sdk/anthropic';
import { google } from '@ai-sdk/google';
import { listFiles, readFile } from '@/lib/fs-tools';

export const maxDuration = 60; // Allow longer responses

export async function POST(req: Request) {
    const { messages } = await req.json();

    const provider = process.env.LLM_PROVIDER || 'openai';
    let model;

    console.log(`Using provider: ${provider}`);

    if (provider === 'google') {
        model = google('gemini-1.5-pro-latest');
    } else if (provider === 'anthropic') {
        model = anthropic('claude-3-5-sonnet-20241022');
    } else {
        // Check if Azure OpenAI configuration is present
        const isAzure = process.env.AZURE_OPENAI_API_KEY &&
            process.env.AZURE_OPENAI_ENDPOINT &&
            process.env.AZURE_OPENAI_DEPLOYMENT_NAME;

        if (isAzure) {
            console.log('Using Azure OpenAI');
            const apiVersion = process.env.AZURE_OPENAI_API_VERSION || '2024-02-15-preview';
            const azureOpenAI = createOpenAI({
                apiKey: process.env.AZURE_OPENAI_API_KEY,
                baseURL: `${process.env.AZURE_OPENAI_ENDPOINT}/openai/deployments/${process.env.AZURE_OPENAI_DEPLOYMENT_NAME}?api-version=${apiVersion}`,
            });
            model = azureOpenAI(process.env.AZURE_OPENAI_DEPLOYMENT_NAME!);
        } else {
            console.log('Using standard OpenAI');
            model = openai('gpt-4o');
        }
    }

    const result = streamText({
        model,
        messages: convertToCoreMessages(messages),
        system: `You are the Knowledge Keeper of the AMODIT R&D Department.
Your goal is to answer the user's questions by exploring the file system.
You DO NOT have a vector database. You must navigate the folders manually.

CRITICAL INSTRUCTIONS:
1. ALWAYS start by reading 'GEMINI.md' to understand the structure of the repository. It is the Master Map.
2. Use the 'list_files' tool to see what is in a directory.
3. Use the 'read_file' tool to read the content of a file.
4. Follow links in files. If 'GEMINI.md' points to 'projekty/README.md', read that file next.
5. If searching for a specific project, look in 'projekty/' folder.
6. If searching for daily notes or meetings, look in 'Notatki/'.
7. Plan your navigation steps. Don't just guess.
8. Be concise in your final answer, but thorough in your research.

Current Repository Root Context:
- The user is asking about the 'AMODIT' project files.
- You are located at the root of the repository.
`,
        tools: {
            list_files: tool({
                description: 'List files and directories in a given path. Use this to explore the folder structure.',
                inputSchema: z.object({
                    path: z.string().describe('The relative path to list, e.g., "projekty" or "." for root.'),
                }),
                execute: async (args) => {
                    const { path } = args;
                    console.log(`Tool: list_files(${path})`);
                    return await listFiles(path);
                },
            }),
            read_file: tool({
                description: 'Read the content of a file. Use this to read documentation, notes, or changelogs.',
                inputSchema: z.object({
                    path: z.string().describe('The relative path to the file, e.g., "GEMINI.md" or "projekty/README.md".'),
                }),
                execute: async (args) => {
                    const { path } = args;
                    console.log(`Tool: read_file(${path})`);
                    return await readFile(path);
                },
            }),
        },
    });

    return result.toTextStreamResponse();
}
