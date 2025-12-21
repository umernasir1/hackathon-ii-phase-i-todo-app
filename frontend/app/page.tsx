export default function Home() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gray-50">
      <div className="w-full max-w-md space-y-8 px-4">
        <div className="text-center">
          <h1 className="text-4xl font-bold tracking-tight text-gray-900">
            Todo App
          </h1>
          <p className="mt-2 text-sm text-gray-600">
            Phase II - Full-Stack Web Application
          </p>
        </div>

        <div className="mt-8 space-y-4">
          <a
            href="/login"
            className="block w-full rounded-md bg-blue-600 px-4 py-3 text-center text-sm font-semibold text-white hover:bg-blue-700"
          >
            Login
          </a>
          <a
            href="/signup"
            className="block w-full rounded-md border border-gray-300 bg-white px-4 py-3 text-center text-sm font-semibold text-gray-700 hover:bg-gray-50"
          >
            Sign Up
          </a>
        </div>

        <div className="mt-6 text-center text-xs text-gray-500">
          <p>
            Built with Next.js 16, FastAPI, and PostgreSQL
          </p>
        </div>
      </div>
    </div>
  )
}
