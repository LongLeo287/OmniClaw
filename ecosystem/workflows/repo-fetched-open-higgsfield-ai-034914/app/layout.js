import './globals.css';

export const metadata = {
  title: 'Open Higgsfield AI — Free AI Image & Video Studio',
  description: 'Generate AI images and videos using 200+ models — Flux, Midjourney, Kling, Veo, Seedance and more. Free open-source alternative to Higgsfield AI.',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
