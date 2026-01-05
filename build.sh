#!/bin/bash
set -e

echo "📦 Installing dependencies in frontend directory..."
cd frontend
npm install

echo "🔨 Building Next.js application..."
npm run build

echo "✅ Build completed successfully!"
