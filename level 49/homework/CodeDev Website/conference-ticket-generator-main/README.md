import React, { useState } from 'react';
import { AlertCircle, Upload } from 'lucide-react';
import { Alert, AlertDescription } from '@/components/ui/alert';

const ConferenceTicketForm = () => {
  const [formData, setFormData] = useState({
    avatar: null,
    fullName: '',
    email: '',
    githubUsername: ''
  });

  const [errors, setErrors] = useState({});
  const [showTicket, setShowTicket] = useState(false);

  const validateForm = () => {
    const newErrors = {};

    if (!formData.fullName.trim()) {
      newErrors.fullName = 'Full name is required';
    }

    if (!formData.email.trim()) {
      newErrors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Please enter a valid email address';
    }

    if (!formData.githubUsername.trim()) {
      newErrors.githubUsername = 'GitHub username is required';
    }

    return newErrors;
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      if (file.size > 500000) {
        setErrors(prev => ({
          ...prev,
          avatar: 'File size must be less than 500KB'
        }));
        return;
      }
      
      if (!['image/jpeg', 'image/png'].includes(file.type)) {
        setErrors(prev => ({
          ...prev,
          avatar: 'Only JPG or PNG files are allowed'
        }));
        return;
      }

      setFormData(prev => ({ ...prev, avatar: file }));
      setErrors(prev => ({ ...prev, avatar: null }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const newErrors = validateForm();
    
    if (Object.keys(newErrors).length === 0) {
      setShowTicket(true);
    } else {
      setErrors(newErrors);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-black p-6">
      <div className="max-w-2xl mx-auto">
        {/* Header */}
        <div className="mb-8 text-center">
          <div className="flex justify-center mb-4">
            <img 
              src="/api/placeholder/48/48"
              alt="Coding Conf Logo"
              className="h-12 w-12"
            />
          </div>
          <h1 className="text-4xl font-bold text-white mb-4">
            Your Journey to Coding Conf 2025 Starts Here!
          </h1>
          <p className="text-gray-300">
            Secure your spot at next year's biggest coding conference.
          </p>
        </div>

        {!showTicket ? (
          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Avatar Upload */}
            <div>
              <label className="block text-white mb-2">Upload Avatar</label>
              <div 
                className="border-2 border-dashed border-gray-600 rounded-lg p-8 text-center cursor-pointer hover:border-gray-400 transition-colors"
                onClick={() => document.getElementById('avatar-upload').click()}
              >
                <Upload className="mx-auto h-12 w-12 text-gray-400 mb-4" />
                <p className="text-gray-300">Drag and drop or click to upload</p>
                <p className="text-sm text-gray-400 mt-2">
                  Upload your photo (JPG or PNG, max size: 500KB)
                </p>
                <input
                  id="avatar-upload"
                  type="file"
                  className="hidden"
                  accept="image/jpeg,image/png"
                  onChange={handleFileUpload}
                  aria-label="Upload avatar"
                />
              </div>
              {errors.avatar && (
                <Alert variant="destructive" className="mt-2">
                  <AlertCircle className="h-4 w-4" />
                  <AlertDescription>{errors.avatar}</AlertDescription>
                </Alert>
              )}
            </div>

            {/* Full Name */}
            <div>
              <label htmlFor="fullName" className="block text-white mb-2">
                Full Name
              </label>
              <input
                id="fullName"
                type="text"
                value={formData.fullName}
                onChange={(e) => setFormData(prev => ({ ...prev, fullName: e.target.value }))}
                className="w-full p-3 rounded-lg bg-purple-900/50 text-white border border-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500"
                aria-invalid={errors.fullName ? "true" : "false"}
              />
              {errors.fullName && (
                <Alert variant="destructive" className="mt-2">
                  <AlertCircle className="h-4 w-4" />
                  <AlertDescription>{errors.fullName}</AlertDescription>
                </Alert>
              )}
            </div>

            {/* Email */}
            <div>
              <label htmlFor="email" className="block text-white mb-2">
                Email Address
              </label>
              <input
                id="email"
                type="email"
                value={formData.email}
                onChange={(e) => setFormData(prev => ({ ...prev, email: e.target.value }))}
                className="w-full p-3 rounded-lg bg-purple-900/50 text-white border border-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500"
                aria-invalid={errors.email ? "true" : "false"}
              />
              {errors.email && (
                <Alert variant="destructive" className="mt-2">
                  <AlertCircle className="h-4 w-4" />
                  <AlertDescription>{errors.email}</AlertDescription>
                </Alert>
              )}
            </div>

            {/* GitHub Username */}
            <div>
              <label htmlFor="githubUsername" className="block text-white mb-2">
                GitHub Username
              </label>
              <div className="relative">
                <span className="absolute left-3 top-3 text-gray-400">@</span>
                <input
                  id="githubUsername"
                  type="text"
                  value={formData.githubUsername}
                  onChange={(e) => setFormData(prev => ({ ...prev, githubUsername: e.target.value }))}
                  className="w-full p-3 pl-8 rounded-lg bg-purple-900/50 text-white border border-purple-700 focus:outline-none focus:ring-2 focus:ring-purple-500"
                  aria-invalid={errors.githubUsername ? "true" : "false"}
                />
              </div>
              {errors.githubUsername && (
                <Alert variant="destructive" className="mt-2">
                  <AlertCircle className="h-4 w-4" />
                  <AlertDescription>{errors.githubUsername}</AlertDescription>
                </Alert>
              )}
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              className="w-full py-3 px-4 bg-coral-500 hover:bg-coral-600 text-white font-semibold rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-coral-500 focus:ring-offset-2"
            >
              Generate My Ticket
            </button>
          </form>
        ) : (
          <div className="bg-purple-900/50 p-8 rounded-lg border border-purple-700">
            <h2 className="text-2xl font-bold text-white mb-4">
              Your Ticket is Ready!
            </h2>
            <div className="flex items-center space-x-4 mb-4">
              {formData.avatar && (
                <img
                  src={URL.createObjectURL(formData.avatar)}
                  alt="Profile"
                  className="h-16 w-16 rounded-full"
                />
              )}
              <div>
                <p className="text-white font-semibold">{formData.fullName}</p>
                <p className="text-gray-300">{formData.email}</p>
                <p className="text-gray-300">@{formData.githubUsername}</p>
              </div>
            </div>
            <button
              onClick={() => setShowTicket(false)}
              className="text-coral-500 hover:text-coral-400 font-medium"
            >
              Edit Information
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default ConferenceTicketForm;