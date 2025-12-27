document$.subscribe(() => {
  // Load Mermaid library if not already loaded by a plugin
  // This might be redundant if mermaid2 plugin already loads it, but ensures it's there.
  if (typeof mermaid === 'undefined') {
    const script = document.createElement('script');
    script.src = 'https://unpkg.com/mermaid@latest/dist/mermaid.min.js';
    document.head.appendChild(script);
    script.onload = () => {
      mermaid.initialize({
        startOnLoad: false, // We will manually start it
        theme: document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "default"
      });
      mermaid.run(); // Manually process diagrams
    };
  } else {
    // If mermaid is already defined, just initialize and run it
    mermaid.initialize({
      startOnLoad: false, // We will manually start it
      theme: document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "default"
    });
    mermaid.run(); // Manually process diagrams
  }
});