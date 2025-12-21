# Todo App - Frontend

Next.js 16+ frontend for the Todo Full-Stack Web Application (Phase II).

## Tech Stack

- **Framework**: Next.js 16+ with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Authentication**: Better Auth
- **Package Manager**: npm/pnpm

## Prerequisites

- Node.js 18+ and npm/pnpm
- Backend API running (see `../backend/README.md`)

## Setup

1. **Install dependencies**
   ```bash
   npm install
   # or
   pnpm install
   ```

2. **Configure environment variables**
   ```bash
   cp .env.example .env.local
   ```

   Edit `.env.local`:
   ```
   NEXT_PUBLIC_API_URL=http://localhost:8000
   BETTER_AUTH_SECRET=your-secret-key-here
   BETTER_AUTH_URL=http://localhost:3000
   ```

3. **Run development server**
   ```bash
   npm run dev
   # or
   pnpm dev
   ```

   Open [http://localhost:3000](http://localhost:3000)

## Development

### Project Structure
```
frontend/
├── app/              # Next.js App Router pages
├── components/       # Reusable UI components
├── lib/              # Utilities and API client
└── public/           # Static assets
```

### Key Files
- `app/page.tsx` - Landing/login page
- `app/dashboard/page.tsx` - Main todo dashboard
- `lib/api.ts` - Backend API client
- `components/tasks/TaskList.tsx` - Task list component

### Available Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

## Features

- User registration and login
- Create, read, update, delete tasks
- Mark tasks as complete/incomplete
- Responsive design (mobile + desktop)
- Protected routes with authentication

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `NEXT_PUBLIC_API_URL` | Backend API base URL | `http://localhost:8000` |
| `BETTER_AUTH_SECRET` | Secret for Better Auth | `your-secret-key` |
| `BETTER_AUTH_URL` | Frontend URL for auth callbacks | `http://localhost:3000` |

## Deployment

### Vercel (Recommended)

1. Push code to GitHub
2. Import repository in Vercel
3. Set environment variables in Vercel dashboard
4. Deploy

## References

- [Next.js Documentation](https://nextjs.org/docs)
- [Better Auth Documentation](https://better-auth.com)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Project Specification](../specs/phase-ii-web-app/spec.md)
- [Implementation Plan](../specs/phase-ii-web-app/plan.md)
