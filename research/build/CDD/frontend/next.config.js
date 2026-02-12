/** @type {import('next').NextConfig} */
const nextConfig = {
  // Enable server actions for CopilotKit
  experimental: {
    serverActions: {
      bodySizeLimit: '2mb',
    },
  },
  // Proxy API requests to backend during development
  async rewrites() {
    return [
      {
        source: '/api/cdd/:path*',
        destination: 'http://localhost:8000/api/cdd/:path*',
      },
    ];
  },
};

module.exports = nextConfig;
