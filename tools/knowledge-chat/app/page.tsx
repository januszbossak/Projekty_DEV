'use client';

import { useChat } from '@ai-sdk/react';
import { Send, Bot, User, Loader2, FolderSearch, FileText } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { useEffect, useRef, useState } from 'react';

export default function ChatPage() {
  const { messages, sendMessage, status } = useChat();
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, status]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || status === 'submitted' || status === 'streaming') return;
    sendMessage({ role: 'user', parts: [{ type: 'text', text: input }] });
    setInput('');
  };

  const isLoading = status === 'submitted' || status === 'streaming';

  // Helper to extract text from message parts
  const getMessageText = (message: typeof messages[0]) => {
    return message.parts
      .filter((part) => part.type === 'text')
      .map((part: any) => part.text)
      .join('');
  };

  return (
    <div className="flex flex-col h-screen bg-zinc-950 text-zinc-50 font-sans">
      {/* Header */}
      <header className="flex items-center px-6 py-4 border-b border-zinc-800 bg-zinc-900/50 backdrop-blur-md">
        <div className="p-2 mr-3 bg-indigo-500/10 rounded-lg">
          <Bot className="w-6 h-6 text-indigo-400" />
        </div>
        <div>
          <h1 className="font-semibold text-lg">AMODIT Knowledge Agent</h1>
          <p className="text-xs text-zinc-500">Agentic File System Navigation</p>
        </div>
      </header>

      {/* Chat Area */}
      <div className="flex-1 overflow-y-auto p-6 space-y-6">
        {messages.length === 0 && (
          <div className="h-full flex flex-col items-center justify-center text-center p-8 opacity-50">
            <Bot className="w-16 h-16 mb-4 text-zinc-600" />
            <p className="text-xl font-medium text-zinc-400">Zadaj pytanie o projekty</p>
            <div className="mt-4 flex gap-2 text-sm text-zinc-600">
              <span className="px-3 py-1 bg-zinc-800 rounded-full">"Co to jest GEMINI.md?"</span>
              <span className="px-3 py-1 bg-zinc-800 rounded-full">"Opisz projekt WIM"</span>
            </div>
          </div>
        )}

        {messages.map((m) => (
          <div
            key={m.id}
            className={`flex w-full max-w-4xl mx-auto gap-4 ${m.role === 'user' ? 'flex-row-reverse' : 'flex-row'
              }`}
          >
            <div
              className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center mt-1 ${m.role === 'user' ? 'bg-indigo-500' : 'bg-zinc-800'
                }`}
            >
              {m.role === 'user' ? <User size={16} /> : <Bot size={16} />}
            </div>

            <div className={`flex flex-col gap-2 min-w-0 max-w-[85%] ${m.role === 'user' ? 'items-end' : 'items-start'}`}>
              <div
                className={`rounded-2xl px-5 py-3 text-sm leading-relaxed shadow-sm ${m.role === 'user'
                  ? 'bg-indigo-500 text-white rounded-tr-none'
                  : 'bg-zinc-800 border border-zinc-700 rounded-tl-none prose prose-invert prose-sm max-w-none break-words'
                  }`}
              >
                {m.parts.map((part, index) => {
                  if (part.type === 'text') {
                    return <ReactMarkdown key={index} remarkPlugins={[remarkGfm]}>{part.text}</ReactMarkdown>;
                  }

                  // Check different possible shapes of tool invocation parts in AI SDK 5.x
                  // Sometimes part is { type: 'tool-invocation', toolInvocation: ... }
                  // Sometimes it acts differently. Let's inspect safely.
                  const toolPart = part as any;

                  if (toolPart.type === 'tool-invocation' || toolPart.toolInvocation) {
                    const toolInvocation = toolPart.toolInvocation || toolPart;
                    const toolCallId = toolInvocation.toolCallId;
                    const toolName = toolInvocation.toolName;
                    const args = toolInvocation.args;
                    const result = toolInvocation.result;

                    if (!toolName) return null; // Skip if no tool name

                    return (
                      <div key={index} className="flex flex-col gap-1 my-2 bg-black/20 p-2 rounded border border-white/5 text-xs text-zinc-400 font-mono">
                        <div className="flex items-center gap-2">
                          {toolName === 'list_files' ? <FolderSearch size={12} /> : <FileText size={12} />}
                          <span className="font-semibold text-indigo-400">{toolName}</span>
                          <span className="opacity-70 truncate max-w-[200px]" title={JSON.stringify(args)}>
                            {JSON.stringify(args).slice(0, 50)}{JSON.stringify(args).length > 50 ? '...' : ''}
                          </span>
                        </div>
                        {!result && (
                          <div className="flex items-center gap-2 text-zinc-500 ml-5">
                            <Loader2 size={10} className="animate-spin" />
                            <span>Working...</span>
                          </div>
                        )}
                        {result && (
                          <div className="ml-5 text-emerald-500 opacity-75">
                            ✓ Done
                          </div>
                        )}
                      </div>
                    );
                  }
                  return null;
                })}
              </div>
            </div>
          </div>
        ))}

        {isLoading && messages[messages.length - 1]?.role === 'user' && (
          <div className="flex w-full max-w-4xl mx-auto gap-4">
            <div className="flex-shrink-0 w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center mt-1">
              <Loader2 size={16} className="animate-spin" />
            </div>
            <div className="flex items-center gap-2 text-xs text-zinc-500 bg-zinc-800/30 px-3 py-1.5 rounded-md animate-pulse">
              Thinking...
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="p-4 border-t border-zinc-800 bg-zinc-900/30 backdrop-blur-md">
        <form onSubmit={handleSubmit} className="relative max-w-4xl mx-auto flex items-center">
          <input
            className="w-full bg-zinc-800/50 text-zinc-100 border border-zinc-700 rounded-xl px-4 py-3 pr-12 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500/50 transition-all placeholder:text-zinc-600"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Zadaj pytanie..."
          />
          <button
            type="submit"
            disabled={isLoading || !input.trim()}
            className="absolute right-2 p-2 bg-indigo-500 text-white rounded-lg hover:bg-indigo-600 disabled:opacity-50 disabled:cursor-not-allowed transition-all active:scale-95"
          >
            <Send size={16} />
          </button>
        </form>
      </div>
    </div>
  );
}
