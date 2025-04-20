document$.subscribe(() => {
  mermaid.initialize({ 
    theme: 'dark',
    startOnLoad: false,
    securityLevel: 'loose'
  });
  mermaid.run({
    querySelector: '.mermaid',
  });
})
