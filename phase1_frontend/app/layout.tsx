import type { Metadata } from "next";
import { Outfit } from "next/font/google";
import "./globals.css";
import { cn } from "@/lib/utils";

const outfit = Outfit({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "AI Mock Interviewer | Master Your Next Job",
  description: "Practice interviews with advanced AI analysis and feedback.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className={cn(outfit.className, "bg-background min-h-screen")}>
        {children}
      </body>
    </html>
  );
}
