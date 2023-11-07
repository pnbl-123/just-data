import { auth } from "@clerk/nextjs";
import Link from "next/link";

export default function HomePage() {
  const { userId } : { userId: string | null } = auth();
  console.log('userId==', userId);
  
  const href = userId ? '/tools' : '/sign-in';

  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-b from-[#2e026d] to-[#15162c] text-white">
      <div className="container flex flex-col items-center justify-center gap-12 px-4 py-16 ">
        <h1 className="text-5xl font-extrabold tracking-tight text-white sm:text-[5rem]">
          Create <span className="text-[hsl(280,100%,70%)]">Tools</span> App
        </h1>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 md:gap-8">
          <Link
            className="flex max-w-xs flex-col gap-4 rounded-xl bg-white/10 p-4 text-white hover:bg-white/20"
            href={href}
          >
            <h3 className="text-2xl font-bold">First Steps →</h3>
            <div className="text-lg">
              Get started
            </div>
          </Link>
        </div>
      </div>
    </main>
  );
}
