import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AMODIT Knowledge Chat",
  description: "Agentic file system navigation for AMODIT R&D knowledge base",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pl" suppressHydrationWarning>
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
