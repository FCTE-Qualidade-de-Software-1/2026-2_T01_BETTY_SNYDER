window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

let typesetting = Promise.resolve();

document$.subscribe(() => {
  typesetting = typesetting
    .then(() => MathJax.startup.promise)
    .then(() => {
      const formulas = Array.from(document.querySelectorAll(".arithmatex"))
        .filter((formula) => !formula.querySelector("mjx-container"));
      if (formulas.length === 0) return;
      return MathJax.typesetPromise(formulas);
    })
    .catch((error) => {
      console.error("Falha ao renderizar fórmulas matemáticas.", error);
    });
});
