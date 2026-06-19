"""CAUGU Web Dashboard - React/Next.js Setup"""

This guide will help you create a web dashboard for CAUGU.

## Setup Instructions

### Prerequisites
- Node.js 16+
- npm or yarn

### Create Project

```bash
npx create-next-app@latest caugu-web --typescript --tailwind
cd caugu-web
```

### Install Dependencies

```bash
npm install axios recharts lucide-react
```

### Project Structure

```
src/
├── components/
│   ├── Dashboard.tsx
│   ├── FitnessChart.tsx
│   ├── ProductCard.tsx
│   └── PinPreview.tsx
├── pages/
│   ├── api/
│   │   ├── workouts.ts
│   │   ├── products.ts
│   │   └── pins.ts
│   ├── index.tsx
│   ├── fitness.tsx
│   ├── affiliate.tsx
│   └── settings.tsx
├── lib/
│   ├── api.ts
│   └── types.ts
└── styles/
    └── globals.css
```

### Run Development Server

```bash
npm run dev
# Visit http://localhost:3000
```

### Build for Production

```bash
npm run build
npm start
```
