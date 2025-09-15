import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';

const App = () => (
  <div className="min-h-screen flex flex-col items-center justify-center p-8">
    <h1 className="text-4xl font-bold text-primary mb-4">S.C.O.U.T. v3</h1>
    <p className="text-neutral max-w-xl text-center">
      Autonomous Hiring Intelligence Platform – frontend scaffold.
    </p>
  </div>
);

createRoot(document.getElementById('root')!).render(<App />);
