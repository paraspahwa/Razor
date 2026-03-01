import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowLeft } from 'lucide-react';

const AvatarLibrary: React.FC = () => {
  return (
    <div className="min-h-screen bg-black text-white p-8">
      <div className="max-w-6xl mx-auto">
        <Link to="/dashboard" className="flex items-center space-x-2 text-gray-400 hover:text-white mb-6">
          <ArrowLeft className="w-5 h-5" />
          <span>Back to Dashboard</span>
        </Link>
        <h1 className="text-3xl font-bold">Avatar  Library</h1>
        <p className="text-gray-400 mt-2">This page is under development.</p>
      </div>
    </div>
  );
};

export default AvatarLibrary;
