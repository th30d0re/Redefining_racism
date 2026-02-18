import './index.css';

function DiagnosticApp() {
  return (
    <div style={{ padding: '2rem', color: 'white' }}>
      <h1>🔧 Diagnostic Check</h1>
      <p>If you can see this, React is working!</p>
      <ul>
        <li>✅ Vite server running</li>
        <li>✅ React rendering</li>
        <li>✅ TypeScript compiling</li>
      </ul>
      <p>Now checking components...</p>
    </div>
  );
}

export default DiagnosticApp;
