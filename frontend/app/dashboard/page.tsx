'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/lib/auth-context'
import { api } from '@/lib/api'
import type { Task, CreateTaskInput, UpdateTaskInput } from '@/lib/types'

export default function DashboardPage() {
  const router = useRouter()
  const { user, token, logout, loading: authLoading } = useAuth()

  const [tasks, setTasks] = useState<Task[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  // New task form
  const [newTask, setNewTask] = useState<CreateTaskInput>({ title: '', description: '' })
  const [adding, setAdding] = useState(false)

  // Edit task
  const [editingTask, setEditingTask] = useState<number | null>(null)
  const [editForm, setEditForm] = useState<UpdateTaskInput>({})

  // Redirect if not logged in
  useEffect(() => {
    if (!authLoading && !user) {
      router.push('/login')
    }
  }, [user, authLoading, router])

  // Fetch tasks
  useEffect(() => {
    if (user && token) {
      fetchTasks()
    }
  }, [user, token])

  const fetchTasks = async () => {
    if (!user || !token) return

    try {
      setLoading(true)
      const response = await api.getTasks(user.id, token)
      setTasks(response.tasks)
      setError('')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load tasks')
    } finally {
      setLoading(false)
    }
  }

  const handleAddTask = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!user || !token || !newTask.title.trim()) return

    setAdding(true)
    try {
      const task = await api.createTask(user.id, newTask, token)
      setTasks([task, ...tasks])
      setNewTask({ title: '', description: '' })
      setError('')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to add task')
    } finally {
      setAdding(false)
    }
  }

  const handleToggleComplete = async (task: Task) => {
    if (!user || !token) return

    try {
      const updated = await api.updateTask(
        user.id,
        task.id,
        { completed: !task.completed },
        token
      )
      setTasks(tasks.map((t) => (t.id === task.id ? updated : t)))
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to update task')
    }
  }

  const handleDeleteTask = async (taskId: number) => {
    if (!user || !token) return
    if (!confirm('Are you sure you want to delete this task?')) return

    try {
      await api.deleteTask(user.id, taskId, token)
      setTasks(tasks.filter((t) => t.id !== taskId))
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to delete task')
    }
  }

  const handleEditTask = (task: Task) => {
    setEditingTask(task.id)
    setEditForm({
      title: task.title,
      description: task.description || '',
    })
  }

  const handleSaveEdit = async (taskId: number) => {
    if (!user || !token) return

    try {
      const updated = await api.updateTask(user.id, taskId, editForm, token)
      setTasks(tasks.map((t) => (t.id === taskId ? updated : t)))
      setEditingTask(null)
      setEditForm({})
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to update task')
    }
  }

  if (authLoading || loading) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <div className="text-gray-600">Loading...</div>
      </div>
    )
  }

  if (!user) {
    return null
  }

  const completedCount = tasks.filter((t) => t.completed).length
  const pendingCount = tasks.length - completedCount

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="mx-auto max-w-4xl px-4 py-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-gray-900">My Tasks</h1>
              <p className="text-sm text-gray-600">{user.email}</p>
            </div>
            <button
              onClick={logout}
              className="rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-semibold text-gray-700 hover:bg-gray-50"
            >
              Logout
            </button>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-4xl px-4 py-8 sm:px-6 lg:px-8">
        {/* Stats */}
        <div className="mb-6 grid grid-cols-2 gap-4 sm:grid-cols-3">
          <div className="rounded-lg bg-white p-4 shadow">
            <p className="text-sm font-medium text-gray-600">Total</p>
            <p className="text-2xl font-bold text-gray-900">{tasks.length}</p>
          </div>
          <div className="rounded-lg bg-white p-4 shadow">
            <p className="text-sm font-medium text-gray-600">Pending</p>
            <p className="text-2xl font-bold text-orange-600">{pendingCount}</p>
          </div>
          <div className="rounded-lg bg-white p-4 shadow">
            <p className="text-sm font-medium text-gray-600">Completed</p>
            <p className="text-2xl font-bold text-green-600">{completedCount}</p>
          </div>
        </div>

        {/* Error message */}
        {error && (
          <div className="mb-4 rounded-md bg-red-50 p-4">
            <p className="text-sm text-red-800">{error}</p>
          </div>
        )}

        {/* Add task form */}
        <div className="mb-6 rounded-lg bg-white p-6 shadow">
          <h2 className="mb-4 text-lg font-semibold text-gray-900">Add New Task</h2>
          <form onSubmit={handleAddTask} className="space-y-4">
            <div>
              <input
                type="text"
                placeholder="Task title"
                value={newTask.title}
                onChange={(e) => setNewTask({ ...newTask, title: e.target.value })}
                className="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-gray-900 focus:border-blue-500 focus:outline-none focus:ring-blue-500"
                required
              />
            </div>
            <div>
              <textarea
                placeholder="Description (optional)"
                value={newTask.description}
                onChange={(e) => setNewTask({ ...newTask, description: e.target.value })}
                className="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-gray-900 focus:border-blue-500 focus:outline-none focus:ring-blue-500"
                rows={2}
              />
            </div>
            <button
              type="submit"
              disabled={adding || !newTask.title.trim()}
              className="w-full rounded-md bg-blue-600 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-700 disabled:bg-blue-400 disabled:cursor-not-allowed sm:w-auto"
            >
              {adding ? 'Adding...' : 'Add Task'}
            </button>
          </form>
        </div>

        {/* Task list */}
        <div className="space-y-3">
          <h2 className="text-lg font-semibold text-gray-900">Your Tasks</h2>
          {tasks.length === 0 ? (
            <div className="rounded-lg bg-white p-8 text-center shadow">
              <p className="text-gray-600">No tasks yet. Add your first task above!</p>
            </div>
          ) : (
            tasks.map((task) => (
              <div
                key={task.id}
                className="rounded-lg bg-white p-4 shadow transition hover:shadow-md"
              >
                {editingTask === task.id ? (
                  <div className="space-y-3">
                    <input
                      type="text"
                      value={editForm.title}
                      onChange={(e) => setEditForm({ ...editForm, title: e.target.value })}
                      className="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-gray-900 focus:border-blue-500 focus:outline-none"
                    />
                    <textarea
                      value={editForm.description}
                      onChange={(e) => setEditForm({ ...editForm, description: e.target.value })}
                      className="w-full rounded-md border border-gray-300 bg-white px-3 py-2 text-gray-900 focus:border-blue-500 focus:outline-none"
                      rows={2}
                    />
                    <div className="flex gap-2">
                      <button
                        onClick={() => handleSaveEdit(task.id)}
                        className="rounded-md bg-blue-600 px-3 py-1 text-sm text-white hover:bg-blue-700"
                      >
                        Save
                      </button>
                      <button
                        onClick={() => setEditingTask(null)}
                        className="rounded-md border border-gray-300 px-3 py-1 text-sm text-gray-700 hover:bg-gray-50"
                      >
                        Cancel
                      </button>
                    </div>
                  </div>
                ) : (
                  <div className="flex items-start gap-3">
                    <input
                      type="checkbox"
                      checked={task.completed}
                      onChange={() => handleToggleComplete(task)}
                      className="mt-1 h-5 w-5 rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                    />
                    <div className="flex-1">
                      <h3
                        className={`font-medium ${
                          task.completed ? 'text-gray-500 line-through' : 'text-gray-900'
                        }`}
                      >
                        {task.title}
                      </h3>
                      {task.description && (
                        <p
                          className={`mt-1 text-sm ${
                            task.completed ? 'text-gray-400' : 'text-gray-600'
                          }`}
                        >
                          {task.description}
                        </p>
                      )}
                      <p className="mt-2 text-xs text-gray-500">
                        {new Date(task.created_at).toLocaleDateString()}
                      </p>
                    </div>
                    <div className="flex gap-2">
                      <button
                        onClick={() => handleEditTask(task)}
                        className="text-sm text-blue-600 hover:text-blue-700"
                      >
                        Edit
                      </button>
                      <button
                        onClick={() => handleDeleteTask(task.id)}
                        className="text-sm text-red-600 hover:text-red-700"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                )}
              </div>
            ))
          )}
        </div>
      </main>
    </div>
  )
}
