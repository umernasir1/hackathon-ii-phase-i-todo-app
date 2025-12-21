# Frontend Development Rules

This is the Next.js 16+ frontend for the Todo Full-Stack Web Application (Phase II).

## Technology Stack

- **Framework**: Next.js 16+ with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Authentication**: Better Auth
- **HTTP Client**: Fetch API / Axios
- **State Management**: React hooks (useState, useEffect)

## Project Structure

```
frontend/
├── app/                    # Next.js App Router
│   ├── layout.tsx         # Root layout with providers
│   ├── page.tsx           # Landing/login page
│   ├── signup/            # Registration page
│   ├── dashboard/         # Main todo dashboard
│   └── api/               # API routes (if needed)
├── components/            # Reusable UI components
│   ├── auth/              # Auth-related components
│   ├── tasks/             # Task-related components
│   └── ui/                # Generic UI components
├── lib/                   # Utilities and helpers
│   ├── api.ts             # API client for backend
│   ├── auth.ts            # Auth utilities
│   └── types.ts           # TypeScript types
├── public/                # Static assets
└── CLAUDE.md              # This file

## Development Guidelines

### 1. Component Structure
- Use functional components with TypeScript
- Prefer server components by default, use 'use client' only when needed
- Keep components small and focused (single responsibility)
- Extract reusable logic into custom hooks

### 2. Type Safety
- Define all types and interfaces in `lib/types.ts`
- Use TypeScript strict mode
- Avoid `any` types - use proper typing or `unknown`
- Export shared types for use across components

### 3. API Communication
- All API calls go through `lib/api.ts`
- Include JWT token in Authorization header
- Handle loading, success, and error states
- Show user-friendly error messages

### 4. Authentication
- Check auth status on protected pages
- Redirect unauthenticated users to login
- Store JWT in httpOnly cookies (via Better Auth)
- Implement logout functionality

### 5. Styling
- Use Tailwind CSS utility classes
- Follow mobile-first responsive design
- Maintain consistent spacing and colors
- Use semantic HTML elements

### 6. Error Handling
- Validate form inputs before submission
- Display validation errors inline
- Handle network errors gracefully
- Provide fallback UI for error states

### 7. Accessibility
- Use semantic HTML (button, nav, main, etc.)
- Include ARIA labels where needed
- Ensure keyboard navigation works
- Maintain color contrast ratios

## Code Standards

### Component Example
```typescript
'use client'

import { useState } from 'react'
import type { Task } from '@/lib/types'

interface TaskListProps {
  tasks: Task[]
  onToggle: (id: number) => Promise<void>
}

export function TaskList({ tasks, onToggle }: TaskListProps) {
  const [loading, setLoading] = useState(false)

  const handleToggle = async (id: number) => {
    setLoading(true)
    try {
      await onToggle(id)
    } catch (error) {
      console.error('Failed to toggle task:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <ul className="space-y-2">
      {tasks.map((task) => (
        <li key={task.id} className="flex items-center gap-2">
          <input
            type="checkbox"
            checked={task.completed}
            onChange={() => handleToggle(task.id)}
            disabled={loading}
          />
          <span className={task.completed ? 'line-through' : ''}>
            {task.title}
          </span>
        </li>
      ))}
    </ul>
  )
}
```

### API Client Example
```typescript
// lib/api.ts
const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

async function fetchWithAuth(url: string, options: RequestInit = {}) {
  const token = await getToken() // From Better Auth

  const response = await fetch(`${API_BASE}${url}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
      ...options.headers,
    },
  })

  if (!response.ok) {
    throw new Error(`API error: ${response.statusText}`)
  }

  return response.json()
}

export const api = {
  getTasks: (userId: string) => fetchWithAuth(`/api/${userId}/tasks`),
  createTask: (userId: string, data: CreateTaskInput) =>
    fetchWithAuth(`/api/${userId}/tasks`, {
      method: 'POST',
      body: JSON.stringify(data),
    }),
  // ... other methods
}
```

## Environment Variables

Create `.env.local` with:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
BETTER_AUTH_SECRET=your-secret-key-here
BETTER_AUTH_URL=http://localhost:3000
```

## Testing Checklist

- [ ] All forms have validation
- [ ] Loading states are shown during API calls
- [ ] Error messages are user-friendly
- [ ] Protected routes redirect to login
- [ ] Responsive on mobile (320px+) and desktop (1920px+)
- [ ] No console errors in browser
- [ ] TypeScript compiles without errors

## References

- Next.js 16 Documentation: https://nextjs.org/docs
- Better Auth Documentation: https://better-auth.com
- Tailwind CSS: https://tailwindcss.com/docs
- Project Spec: `../specs/phase-ii-web-app/spec.md`
- Implementation Plan: `../specs/phase-ii-web-app/plan.md`
- Task List: `../specs/phase-ii-web-app/tasks.md`
