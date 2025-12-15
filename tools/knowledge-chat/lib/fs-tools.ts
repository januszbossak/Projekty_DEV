import fs from 'fs/promises';
import path from 'path';

// Assume the app is in tools/knowledge-chat, so root is two levels up
const REPO_ROOT = path.resolve(process.cwd(), '../..');

export const safePath = (p: string) => {
  const resolved = path.resolve(REPO_ROOT, p.startsWith('/') ? p.slice(1) : p);
  if (!resolved.startsWith(REPO_ROOT)) {
    throw new Error(`Access denied: ${resolved} is outside repository root.`);
  }
  return resolved;
};

export const listFiles = async (dirPath: string) => {
  try {
    const fullPath = safePath(dirPath);
    const items = await fs.readdir(fullPath, { withFileTypes: true });
    return items.map((item) => ({
      name: item.name,
      type: item.isDirectory() ? 'directory' : 'file',
      path: path.relative(REPO_ROOT, path.join(fullPath, item.name)),
    })).sort((a, b) => {
        // Diderectory first
        if (a.type === 'directory' && b.type === 'file') return -1;
        if (a.type === 'file' && b.type === 'directory') return 1;
        return a.name.localeCompare(b.name);
    });
  } catch (error) {
     if ((error as any).code === 'ENOENT') {
         return []
     }
    throw error;
  }
};

export const readFile = async (filePath: string) => {
  const fullPath = safePath(filePath);
  // Limit file size read? Maybe. For now, just read.
  const content = await fs.readFile(fullPath, 'utf-8');
  return content;
};
