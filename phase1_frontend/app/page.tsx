import Link from "next/link";
import { ArrowRight, FileText, Mic, BarChart3 } from "lucide-react";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center relative overflow-hidden bg-background">
      {/* Background Gradient */}
      <div className="absolute inset-0 bg-grid-white/[0.02] bg-[size:50px_50px]" />
      <div className="absolute h-[500px] w-[500px] bg-primary/20 blur-[120px] rounded-full -top-20 -left-20 animate-pulse delay-75" />
      <div className="absolute h-[500px] w-[500px] bg-blue-500/10 blur-[120px] rounded-full bottom-0 right-0 animate-pulse" />

      <div className="z-10 container px-4 md:px-6 flex flex-col items-center text-center space-y-8 pt-20 pb-16">
        <div className="space-y-4 max-w-4xl mx-auto">
          <div className="inline-flex items-center rounded-full border border-primary/20 bg-primary/10 px-3 py-1 text-sm font-medium text-primary mb-4 backdrop-blur-sm">
            <span className="flex h-2 w-2 rounded-full bg-primary mr-2 animate-ping"></span>
            AI-Powered Interview Coach
          </div>
          <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold tracking-tighter bg-clip-text text-transparent bg-gradient-to-b from-white to-white/60">
            Master Your Next <br />
            <span className="text-primary glow-text">Interview</span>
          </h1>
          <p className="mx-auto max-w-[700px] text-muted-foreground md:text-xl leading-relaxed">
            Upload your resume, face challenging AI-generated questions, and get instant, detailed feedback to land your dream job.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row gap-4 w-full sm:w-auto mt-8">
          <Link
            href="/resume"
            className="inline-flex h-12 items-center justify-center rounded-full bg-primary px-8 text-base font-medium text-white shadow-lg shadow-primary/25 transition-all hover:bg-primary/90 hover:scale-105 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring"
          >
            Start Interview <ArrowRight className="ml-2 h-5 w-5" />
          </Link>
          <Link
            href="/example"
            className="inline-flex h-12 items-center justify-center rounded-full border border-white/10 bg-white/5 backdrop-blur-sm px-8 text-base font-medium shadow-sm transition-colors hover:bg-white/10 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring"
          >
            View Example
          </Link>
        </div>
      </div>

      {/* Features Grid */}
      <div className="z-10 container px-4 md:px-6 py-16">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          <FeatureCard
            icon={<FileText className="h-8 w-8 text-blue-400" />}
            title="Resume Analysis"
            description="Our AI parses your resume to tailor questions specifically to your experience."
          />
          <FeatureCard
            icon={<Mic className="h-8 w-8 text-primary" />}
            title="Realistic Interview"
            description="Answer technical and behavioral questions in a realistic chat or voice environment."
          />
          <FeatureCard
            icon={<BarChart3 className="h-8 w-8 text-green-400" />}
            title="Instant Feedback"
            description="Get detailed scoring on relevance, clarity, and confidence."
          />
        </div>
      </div>
    </main>
  );
}

function FeatureCard({ icon, title, description }: { icon: React.ReactNode, title: string, description: string }) {
  return (
    <div className="group relative overflow-hidden rounded-3xl border border-white/5 bg-gradient-to-b from-white/10 to-transparent p-8 transition-all hover:border-white/10 hover:shadow-2xl hover:shadow-primary/5">
      <div className="mb-6 rounded-2xl bg-white/5 w-16 h-16 flex items-center justify-center ring-1 ring-white/10 group-hover:scale-110 transition-transform duration-300">
        {icon}
      </div>
      <h3 className="text-2xl font-bold mb-3">{title}</h3>
      <p className="text-base text-muted-foreground leading-relaxed">{description}</p>
    </div>
  )
}
