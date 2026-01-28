"use client";

import Link from "next/link";
import { ArrowLeft, Home, Star, CheckCircle2, ChevronRight } from "lucide-react";
import { cn } from "@/lib/utils";

export default function ExamplePage() {
    const mockQuestions = [
        {
            text: "Explain the difference between useMemo and useCallback in React.",
            type: "technical",
            difficulty: "medium",
            score: 9,
            answer: "useMemo is used to memoize a computed value to avoid expensive recalculations on every render, while useCallback is used to memoize a function definition to prevent unnecessary re-renders of child components that depend on reference equality for props.",
            feedback: "Excellent explanation. You clearly distinguished between values and functions.",
            improvements: "You could mention that useCallback(fn, deps) is equivalent to useMemo(() => fn, deps).",
            ideal: "useMemo returns a memoized value. useCallback returns a memoized version of a callback that only changes if one of the dependencies has changed."
        },
        {
            text: "Tell me about a time you had a conflict with a coworker.",
            type: "behavioral",
            difficulty: "easy",
            score: 7,
            answer: "We disagreed on the architecture of a new feature. I decided to listen to their point of view, and we eventually found a middle ground that satisfied both our requirements.",
            feedback: "Good use of the STAR method, though a bit brief. You showed emotional intelligence.",
            improvements: "Try to be more specific about the 'middle ground' and the positive impact on the project's timeline or quality.",
            ideal: "Focus on active listening, data-driven decision making, and the successful resolution that benefited the team's goals."
        }
    ];

    const averageScore = 8.0;

    return (
        <div className="min-h-screen flex flex-col items-center p-4 py-20 bg-background text-foreground animate-in fade-in duration-700">
            <div className="w-full max-w-3xl space-y-12">
                <div className="flex items-center justify-between">
                    <Link href="/" className="inline-flex items-center text-sm font-medium text-muted-foreground hover:text-primary transition-colors">
                        <ArrowLeft className="mr-2 h-4 w-4" /> Back to Home
                    </Link>
                    <div className="px-4 py-1.5 rounded-full bg-primary/10 border border-primary/20 text-xs font-bold uppercase tracking-widest text-primary">
                        Sample Result
                    </div>
                </div>

                <div className="text-center space-y-4">
                    <h1 className="text-4xl md:text-5xl font-black tracking-tighter">🎉 Reviewing Example</h1>
                    <p className="text-muted-foreground text-lg max-w-xl mx-auto">
                        This is what a completed interview looks like. High-quality feedback helps you refine your answers.
                    </p>
                </div>

                {/* Score Summary Card */}
                <div className="relative group">
                    <div className="absolute -inset-1 bg-gradient-to-r from-primary to-blue-600 rounded-[2rem] blur opacity-25 group-hover:opacity-40 transition duration-1000"></div>
                    <div className="relative p-8 rounded-3xl border bg-card/50 backdrop-blur-xl shadow-2xl flex flex-col md:flex-row items-center gap-8">
                        <div className="flex-1 text-center md:text-left space-y-2">
                            <h2 className="text-2xl font-bold italic text-muted-foreground">Overall Performance</h2>
                            <p className="text-sm text-muted-foreground max-w-xs uppercase tracking-widest font-bold">Excellent readiness for a Mid-Level Role</p>
                        </div>
                        <div className="h-32 w-32 rounded-full border-8 border-primary/10 flex items-center justify-center relative">
                            <svg className="w-full h-full -rotate-90">
                                <circle
                                    cx="64" cy="64" r="56"
                                    fill="none" stroke="currentColor" strokeWidth="8"
                                    className="text-primary"
                                    strokeDasharray="351.8"
                                    strokeDashoffset={351.8 * (1 - averageScore / 10)}
                                    strokeLinecap="round"
                                />
                            </svg>
                            <span className="absolute text-3xl font-black">{averageScore}</span>
                        </div>
                        <div className="flex flex-col gap-2 shrink-0">
                            <div className="flex items-center gap-2 px-4 py-2 rounded-xl bg-green-500/10 text-green-500 text-sm font-bold">
                                <Star className="h-4 w-4 fill-current" /> Strong Technical
                            </div>
                            <div className="flex items-center gap-2 px-4 py-2 rounded-xl bg-blue-500/10 text-blue-500 text-sm font-bold">
                                <Star className="h-4 w-4 fill-current" /> Clear Communication
                            </div>
                        </div>
                    </div>
                </div>

                {/* Breakdown */}
                <div className="space-y-6">
                    <h3 className="text-2xl font-bold px-2">Question Breakdown</h3>
                    {mockQuestions.map((q, idx) => (
                        <div key={idx} className="space-y-6 p-8 rounded-3xl border bg-card/30 hover:bg-card/50 transition-all duration-300">
                            <div className="flex items-start justify-between gap-4">
                                <div className="space-y-1">
                                    <h4 className="text-xl font-bold leading-tight">{q.text}</h4>
                                    <div className="flex gap-2">
                                        <span className="text-xs font-bold uppercase tracking-wider text-muted-foreground">{q.type}</span>
                                        <span className="text-xs text-muted-foreground">/</span>
                                        <span className="text-xs font-bold uppercase tracking-wider text-muted-foreground">{q.difficulty}</span>
                                    </div>
                                </div>
                                <div className="text-4xl font-black text-primary shrink-0">{q.score}<span className="text-sm text-muted-foreground opacity-50">/10</span></div>
                            </div>

                            <div className="p-5 rounded-2xl bg-secondary/30 italic text-foreground/80 border-l-4 border-primary/40 relative overflow-hidden group">
                                <div className="absolute top-0 right-0 p-2 opacity-10 group-hover:opacity-20 transition-opacity">
                                    <Home className="h-12 w-12" />
                                </div>
                                <p className="text-xs font-black uppercase text-muted-foreground mb-2">Detailed Answer</p>
                                "{q.answer}"
                            </div>

                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div className="space-y-2 p-5 rounded-2xl bg-primary/5 border border-primary/10">
                                    <h5 className="text-xs font-black uppercase text-primary tracking-widest">Growth Feedback</h5>
                                    <p className="text-sm leading-relaxed">{q.feedback}</p>
                                </div>
                                <div className="space-y-2 p-5 rounded-2xl bg-yellow-500/5 border border-yellow-500/10">
                                    <h5 className="text-xs font-black uppercase text-yellow-500 tracking-widest">Key Improvements</h5>
                                    <p className="text-sm leading-relaxed">{q.improvements}</p>
                                </div>
                            </div>

                            <div className="p-5 rounded-2xl bg-blue-500/5 border border-blue-500/10">
                                <h5 className="text-xs font-black uppercase text-blue-500 tracking-widest mb-1">Benchmark Answer</h5>
                                <p className="text-sm leading-relaxed text-blue-500/80">{q.ideal}</p>
                            </div>
                        </div>
                    ))}
                </div>

                <div className="flex flex-col sm:flex-row gap-4 pt-8">
                    <Link href="/resume" className="flex-1 inline-flex h-14 items-center justify-center rounded-full bg-primary text-lg font-bold text-white shadow-xl shadow-primary/25 hover:scale-105 transition-all">
                        Try It Yourself <ChevronRight className="ml-2 h-5 w-5" />
                    </Link>
                    <Link href="/" className="flex-1 inline-flex h-14 items-center justify-center rounded-full border border-white/10 bg-white/5 backdrop-blur-sm text-lg font-medium hover:bg-white/10 transition-colors">
                        Back Home
                    </Link>
                </div>
            </div>
        </div>
    );
}
