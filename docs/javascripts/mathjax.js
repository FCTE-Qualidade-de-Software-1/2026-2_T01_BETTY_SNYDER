window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  startup: {
    typeset: false
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  MathJax.startup.promise
    .then(() => {
      MathJax.typesetClear();
      return MathJax.typesetPromise();
    })
    .catch((error) => {
      console.error("Falha ao renderizar fórmulas matemáticas.", error);
    });
});
