(() => {
  const decks = [
    { id: "teste-1", name: "Teste 1", novo: 0, aprender: 2, revisar: 1 },
    { id: "teste-2", name: "Teste 2", novo: 0, aprender: 3, revisar: 0 },
  ];

  let selectedId = "teste-2";

  const deckList = document.getElementById("deck-list");
  const menuDeck = document.getElementById("menu-deck");
  const overlayCreate = document.getElementById("overlay-create");
  const dialogCreate = document.getElementById("dialog-create");
  const overlayAdd = document.getElementById("overlay-add");
  const dialogAdd = document.getElementById("dialog-add");
  const inputDeckName = document.getElementById("input-deck-name");
  const btnCreateOk = document.getElementById("dialog-create-ok");
  const addDeckBtn = document.getElementById("add-deck-btn");
  const addFront = document.getElementById("add-front");
  const addBack = document.getElementById("add-back");
  const screenDecks = document.getElementById("screen-decks");
  const screenOptions = document.getElementById("screen-options");
  const optionsTitle = document.getElementById("options-title");
  const app = document.getElementById("app");
  const taskbar = document.getElementById("taskbar");
  const tourOverlay = document.getElementById("tour-overlay");
  const tourSpotlight = document.getElementById("tour-spotlight");
  const tourTitle = document.getElementById("tour-title");
  const tourBody = document.getElementById("tour-body");
  const tourStepLabel = document.getElementById("tour-step-label");
  const tourProgressBar = document.getElementById("tour-progress-bar");
  const tourPrev = document.getElementById("tour-prev");
  const tourNext = document.getElementById("tour-next");
  const tourSkip = document.getElementById("tour-skip");
  const tourCard = document.getElementById("tour-card");

  const windowState = {
    main: { minimized: false, maximized: true, closed: false },
    "dialog-create": { minimized: false, maximized: false, closed: true },
    "dialog-add": { minimized: false, maximized: false, closed: true },
    options: { minimized: false, maximized: false, closed: true },
  };

  const tourSteps = [
    {
      title: "Bem-vindo ao Anki",
      target: null,
      body: `
        <p>Este tutorial apresenta os conceitos principais do Anki, um programa de cartões de memória com repetição espaçada, e a melhoria adotada neste protótipo.</p>
        <p><strong>Mudança principal:</strong> ao abrir o aplicativo, a tela inicial já exibe a <strong>lista de baralhos</strong>, sem a etapa intermediária de Início.</p>
        <p>O objetivo é reduzir o tempo necessário para compreender onde estudar e qual ação tomar em seguida.</p>
      `,
    },
    {
      title: "Tela inicial: lista de baralhos",
      target: "deck-list",
      body: `
        <p>Um <strong>baralho</strong> é um conjunto de cartões de estudo. Prefira temas amplos, como "Francês", em vez de uma pasta para cada lição.</p>
        <p>O título <strong>Cartões</strong> agrupa apenas as contagens do dia:</p>
        <ul>
          <li><strong>Novos</strong>: ainda não estudados</li>
          <li><strong>A aprender</strong>: em aprendizado recente</li>
          <li><strong>A revisar</strong>: já aprendidos e com revisão prevista para hoje</li>
        </ul>
      `,
    },
    {
      title: "Criar um baralho",
      target: "criar",
      body: `
        <p>Use <strong>Criar Baralho</strong> para organizar um novo conjunto de cartões.</p>
      `,
    },
    {
      title: "Opções do baralho",
      target: "deck-list",
      body: `
        <p>Selecione um baralho e clique na <strong>engrenagem</strong> para renomear, exportar, excluir ou abrir <strong>Opções do baralho</strong>.</p>
        <p>Nas opções, você define limites diários, como quantidade de cartões novos e revisões máximas por dia.</p>
      `,
    },
    {
      title: "Como estudar",
      target: "deck-list",
      body: `
        <p>Ao escolher um baralho, o estudo começa. Para cada cartão:</p>
        <ul>
          <li>Leia a pergunta e tente responder</li>
          <li>Mostre a resposta com o botão correspondente ou com a tecla Espaço</li>
          <li>Avalie com <strong>De novo</strong>, <strong>Difícil</strong>, <strong>Bom</strong> ou <strong>Fácil</strong></li>
        </ul>
        <p>O Anki agenda a próxima revisão conforme essa avaliação.</p>
      `,
    },
    {
      title: "Começar com conteúdo",
      target: "bottom-actions",
      body: `
        <p>Três caminhos oficiais para iniciar:</p>
        <ul>
          <li><strong>Obter compartilhados</strong>: baixar um baralho pronto</li>
          <li><strong>Importar arquivo</strong>: trazer um pacote <code>.apkg</code></li>
          <li><strong>Adicionar</strong>: criar suas próprias notas e cartões</li>
        </ul>
        <p>Em assuntos complexos, é recomendável criar cartões a partir de material que você já compreende.</p>
      `,
    },
    {
      title: "Pronto para explorar",
      target: "nav",
      body: `
        <p>Você já conhece a lista inicial de baralhos, a criação de baralho, as opções e o significado de Novos, A aprender e A revisar.</p>
        <p>Reabra este tutorial em <strong>Ajuda</strong>. Manual oficial:
          <a href="https://docs.ankiweb.net/manual/getting-started" target="_blank" rel="noopener">Getting Started</a>
          e
          <a href="https://docs.ankiweb.net/manual/studying" target="_blank" rel="noopener">Studying</a>.</p>
      `,
    },
  ];

  let tourIndex = 0;
  let tourActive = false;

  function selectedDeck() {
    return decks.find((d) => d.id === selectedId);
  }

  function syncAddDeckLabel() {
    const deck = selectedDeck();
    if (deck) addDeckBtn.textContent = deck.name;
  }

  function countClass(value, kind) {
    if (kind === "novo") return "deck-row__new";
    if (kind === "aprender") {
      return value === 0 ? "deck-row__learn is-zero" : "deck-row__learn";
    }
    return value === 0 ? "deck-row__review is-zero" : "deck-row__review";
  }

  function renderDecks() {
    deckList.innerHTML = "";
    decks.forEach((deck) => {
      const row = document.createElement("button");
      row.type = "button";
      row.className = `deck-row${deck.id === selectedId ? " is-selected" : ""}`;
      row.dataset.id = deck.id;
      row.setAttribute("role", "listitem");
      row.innerHTML = `
        <span class="deck-row__name">${deck.name}</span>
        <span class="${countClass(deck.novo, "novo")}">${deck.novo}</span>
        <span class="${countClass(deck.aprender, "aprender")}">${deck.aprender}</span>
        <span class="${countClass(deck.revisar, "revisar")}">${deck.revisar}</span>
        <span class="deck-row__gear" data-gear="${deck.id}" title="Opções">
          <img src="assets/gear-icon.png" width="22" height="22" alt="" />
        </span>
      `;

      row.addEventListener("click", (event) => {
        const gear = event.target.closest("[data-gear]");
        if (gear) {
          event.stopPropagation();
          selectedId = deck.id;
          syncAddDeckLabel();
          renderDecks();
          openDeckMenu(gear);
          return;
        }
        selectedId = deck.id;
        syncAddDeckLabel();
        closeMenus();
        renderDecks();
      });

      deckList.appendChild(row);
    });
  }

  function closeMenus() {
    menuDeck.classList.add("hidden");
  }

  function openDeckMenu(gearEl) {
    const row = gearEl.closest(".deck-row");
    const panel = document.getElementById("deck-panel");
    const panelRect = panel.getBoundingClientRect();
    const gearRect = gearEl.getBoundingClientRect();
    const screenRect = screenDecks.getBoundingClientRect();

    menuDeck.classList.remove("hidden");
    menuDeck.style.left = `${gearRect.right - screenRect.left + 8}px`;
    menuDeck.style.top = `${row.getBoundingClientRect().top - screenRect.top}px`;

    const menuWidth = 216;
    if (gearRect.right + menuWidth + 16 > panelRect.right) {
      menuDeck.style.left = `${panelRect.right - screenRect.left - menuWidth}px`;
    }
  }

  function openCreateDialog() {
    closeMenus();
    windowState["dialog-create"] = { minimized: false, maximized: false, closed: false };
    dialogCreate.classList.remove("is-minimized", "is-maximized");
    overlayCreate.classList.remove("hidden");
    overlayCreate.setAttribute("aria-hidden", "false");
    inputDeckName.value = "";
    btnCreateOk.disabled = true;
    renderTaskbar();
    updateMaxButtons();
    inputDeckName.focus();
  }

  function closeCreateDialog() {
    windowState["dialog-create"].closed = true;
    windowState["dialog-create"].minimized = false;
    windowState["dialog-create"].maximized = false;
    dialogCreate.classList.remove("is-minimized", "is-maximized");
    overlayCreate.classList.add("hidden");
    overlayCreate.setAttribute("aria-hidden", "true");
    renderTaskbar();
  }

  function createDeck() {
    const name = inputDeckName.value.trim();
    if (!name) return;
    const id = `deck-${Date.now()}`;
    decks.push({ id, name, novo: 0, aprender: 0, revisar: 0 });
    selectedId = id;
    syncAddDeckLabel();
    closeCreateDialog();
    renderDecks();
  }

  function openAddDialog() {
    closeMenus();
    syncAddDeckLabel();
    windowState["dialog-add"] = { minimized: false, maximized: false, closed: false };
    dialogAdd.classList.remove("is-minimized", "is-maximized");
    overlayAdd.classList.remove("hidden");
    overlayAdd.setAttribute("aria-hidden", "false");
    addFront.value = "";
    addBack.value = "";
    document.getElementById("add-tags").value = "";
    renderTaskbar();
    updateMaxButtons();
    addFront.focus();
  }

  function closeAddDialog() {
    windowState["dialog-add"].closed = true;
    windowState["dialog-add"].minimized = false;
    windowState["dialog-add"].maximized = false;
    dialogAdd.classList.remove("is-minimized", "is-maximized");
    overlayAdd.classList.add("hidden");
    overlayAdd.setAttribute("aria-hidden", "true");
    renderTaskbar();
  }

  function addCard() {
    const front = addFront.value.trim();
    const back = addBack.value.trim();
    if (!front || !back) {
      window.alert("Preencha Frente e Verso para adicionar o cartão.");
      return;
    }
    const deck = selectedDeck();
    if (deck) deck.novo += 1;
    renderDecks();
    addFront.value = "";
    addBack.value = "";
    addFront.focus();
  }

  function openOptions() {
    const deck = selectedDeck();
    if (!deck) return;
    closeMenus();
    optionsTitle.textContent = `Opções para ${deck.name}`;
    windowState.options = { minimized: false, maximized: false, closed: false };
    screenOptions.classList.remove("hidden", "is-minimized", "is-maximized");
    screenDecks.classList.add("hidden");
    renderTaskbar();
    updateMaxButtons();
  }

  function closeOptions() {
    windowState.options.closed = true;
    windowState.options.minimized = false;
    windowState.options.maximized = false;
    screenOptions.classList.add("hidden");
    screenOptions.classList.remove("is-minimized", "is-maximized");
    screenDecks.classList.remove("hidden");
    renderTaskbar();
  }

  function renameSelected() {
    const deck = selectedDeck();
    if (!deck) return;
    const name = window.prompt("Novo nome do baralho:", deck.name);
    if (!name || !name.trim()) return;
    deck.name = name.trim();
    syncAddDeckLabel();
    closeMenus();
    renderDecks();
  }

  function deleteSelected() {
    if (decks.length <= 1) {
      window.alert("Mantenha ao menos um baralho no protótipo.");
      return;
    }
    const deck = selectedDeck();
    if (!deck) return;
    if (!window.confirm(`Excluir o baralho "${deck.name}"?`)) return;
    const index = decks.findIndex((d) => d.id === selectedId);
    decks.splice(index, 1);
    selectedId = decks[0].id;
    syncAddDeckLabel();
    closeMenus();
    renderDecks();
  }

  function updateMaxButtons() {
    document.querySelectorAll("[data-window-controls]").forEach((group) => {
      const id = group.getAttribute("data-window-controls");
      const state = windowState[id];
      const maxBtn = group.querySelector('[data-win="maximize"]');
      if (!maxBtn || !state) return;
      const restore = Boolean(state.maximized);
      maxBtn.setAttribute("aria-label", restore ? "Restaurar" : "Expandir");
      maxBtn.title = restore ? "Restaurar" : "Expandir";
    });
  }

  function renderTaskbar() {
    taskbar.innerHTML = "";
    const chips = [];

    if (windowState.main.minimized || windowState.main.closed) {
      chips.push({
        id: "main",
        label: windowState.main.closed ? "Anki (fechado)" : "Usuário 1 - Anki",
      });
    }
    if (windowState["dialog-create"].minimized && !windowState["dialog-create"].closed) {
      chips.push({ id: "dialog-create", label: "Criar Baralho" });
    }
    if (windowState["dialog-add"].minimized && !windowState["dialog-add"].closed) {
      chips.push({ id: "dialog-add", label: "Adicionar" });
    }
    if (windowState.options.minimized && !windowState.options.closed) {
      chips.push({ id: "options", label: optionsTitle.textContent || "Opções" });
    }

    chips.forEach((chip) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "taskbar__chip";
      btn.innerHTML = `<img src="assets/anki-logo.png" alt="" /><span>${chip.label}</span>`;
      btn.addEventListener("click", () => restoreWindow(chip.id));
      taskbar.appendChild(btn);
    });
  }

  function restoreWindow(id) {
    if (id === "main") {
      windowState.main.minimized = false;
      windowState.main.closed = false;
      app.classList.remove("is-minimized", "is-closed");
    }
    if (id === "dialog-create") {
      windowState["dialog-create"].minimized = false;
      dialogCreate.classList.remove("is-minimized");
      overlayCreate.classList.remove("hidden");
      overlayCreate.setAttribute("aria-hidden", "false");
      inputDeckName.focus();
    }
    if (id === "dialog-add") {
      windowState["dialog-add"].minimized = false;
      dialogAdd.classList.remove("is-minimized");
      overlayAdd.classList.remove("hidden");
      overlayAdd.setAttribute("aria-hidden", "false");
      addFront.focus();
    }
    if (id === "options") {
      windowState.options.minimized = false;
      screenOptions.classList.remove("hidden", "is-minimized");
      screenDecks.classList.add("hidden");
    }
    renderTaskbar();
    updateMaxButtons();
  }

  function handleWindowAction(windowId, action) {
    const state = windowState[windowId];
    if (!state) return;

    if (action === "minimize") {
      state.minimized = true;
      if (windowId === "main") app.classList.add("is-minimized");
      else if (windowId === "dialog-create") {
        dialogCreate.classList.add("is-minimized");
        overlayCreate.classList.add("hidden");
      } else if (windowId === "dialog-add") {
        dialogAdd.classList.add("is-minimized");
        overlayAdd.classList.add("hidden");
      } else if (windowId === "options") {
        screenOptions.classList.add("is-minimized", "hidden");
        screenDecks.classList.remove("hidden");
      }
      renderTaskbar();
      return;
    }

    if (action === "maximize") {
      state.maximized = !state.maximized;
      if (windowId === "main") app.classList.toggle("is-maximized", state.maximized);
      else if (windowId === "dialog-create") dialogCreate.classList.toggle("is-maximized", state.maximized);
      else if (windowId === "dialog-add") dialogAdd.classList.toggle("is-maximized", state.maximized);
      else if (windowId === "options") screenOptions.classList.toggle("is-maximized", state.maximized);
      updateMaxButtons();
      return;
    }

    if (action === "close") {
      if (windowId === "main") {
        state.closed = true;
        state.minimized = false;
        app.classList.add("is-closed");
        app.classList.remove("is-minimized");
        closeCreateDialog();
        closeAddDialog();
        if (!windowState.options.closed) closeOptions();
        renderTaskbar();
        return;
      }
      if (windowId === "dialog-create") {
        closeCreateDialog();
        return;
      }
      if (windowId === "dialog-add") {
        closeAddDialog();
        return;
      }
      if (windowId === "options") closeOptions();
    }
  }

  function clearTourHighlights() {
    document.querySelectorAll(".tour-target-pulse").forEach((el) => {
      el.classList.remove("tour-target-pulse");
    });
    tourSpotlight.hidden = true;
  }

  function overlaps(a, b, gap = 12) {
    return !(
      a.right + gap <= b.left ||
      a.left >= b.right + gap ||
      a.bottom + gap <= b.top ||
      a.top >= b.bottom + gap
    );
  }

  function placeTourCard(targetRect) {
    const margin = 12;
    const gap = 16;
    const vw = window.innerWidth;
    const vh = window.innerHeight;
    const cardWidth = Math.min(560, vw - margin * 2);

    tourCard.style.width = `${cardWidth}px`;
    tourCard.style.maxHeight = "none";
    tourCard.style.overflow = "visible";

    const cardHeight = Math.max(tourCard.getBoundingClientRect().height, 200);

    const tryPlace = (left, top) => {
      const l = Math.min(Math.max(margin, left), vw - cardWidth - margin);
      const t = Math.min(Math.max(margin, top), vh - cardHeight - margin);
      const cardRect = { left: l, top: t, right: l + cardWidth, bottom: t + cardHeight };
      if (targetRect && overlaps(cardRect, targetRect, gap)) return null;
      return { left: l, top: t };
    };

    let chosen = null;

    if (!targetRect) {
      chosen = tryPlace((vw - cardWidth) / 2, vh - cardHeight - margin);
    } else {
      const spaces = [
        {
          // abaixo
          left: targetRect.left + (targetRect.right - targetRect.left - cardWidth) / 2,
          top: targetRect.bottom + gap,
          freeH: vh - margin - (targetRect.bottom + gap),
          freeW: vw - 2 * margin,
        },
        {
          // acima
          left: targetRect.left + (targetRect.right - targetRect.left - cardWidth) / 2,
          top: targetRect.top - cardHeight - gap,
          freeH: targetRect.top - gap - margin,
          freeW: vw - 2 * margin,
        },
        {
          // direita
          left: targetRect.right + gap,
          top: targetRect.top,
          freeH: vh - 2 * margin,
          freeW: vw - margin - (targetRect.right + gap),
        },
        {
          // esquerda
          left: targetRect.left - cardWidth - gap,
          top: targetRect.top,
          freeH: vh - 2 * margin,
          freeW: targetRect.left - gap - margin,
        },
      ];

      // Prefere espaços que realmente cabem o card
      spaces.sort((a, b) => {
        const aOk = a.freeH >= cardHeight && a.freeW >= cardWidth ? 1 : 0;
        const bOk = b.freeH >= cardHeight && b.freeW >= cardWidth ? 1 : 0;
        if (aOk !== bOk) return bOk - aOk;
        return b.freeH * b.freeW - a.freeH * a.freeW;
      });

      for (const space of spaces) {
        if (space.freeH < cardHeight - 4 || space.freeW < cardWidth - 4) continue;
        const ok = tryPlace(space.left, space.top);
        if (ok) {
          chosen = ok;
          break;
        }
      }

      // Cantos livres
      if (!chosen) {
        const corners = [
          [vw - cardWidth - margin, vh - cardHeight - margin],
          [margin, vh - cardHeight - margin],
          [vw - cardWidth - margin, margin],
          [margin, margin],
        ];
        for (const [l, t] of corners) {
          const ok = tryPlace(l, t);
          if (ok) {
            chosen = ok;
            break;
          }
        }
      }
    }

    if (!chosen) {
      const h = tourCard.getBoundingClientRect().height;
      chosen = {
        left: margin,
        top: Math.max(margin, vh - h - margin),
      };
      if (targetRect && overlaps(
        { left: chosen.left, top: chosen.top, right: chosen.left + cardWidth, bottom: chosen.top + h },
        targetRect,
        gap
      )) {
        chosen.top = margin;
      }
    }

    tourCard.style.left = `${chosen.left}px`;
    tourCard.style.top = `${chosen.top}px`;
  }

  function readBorderRadius(el) {
    const style = window.getComputedStyle(el);
    const radius = style.borderRadius || "0px";
    if (radius && radius !== "0px") return radius;
    return style.borderTopLeftRadius || "0px";
  }

  function positionSpotlight(targetKey) {
    clearTourHighlights();
    let targetRect = null;

    if (targetKey) {
      const el = document.querySelector(`[data-tour="${targetKey}"]`);
      if (el) {
        const rect = el.getBoundingClientRect();
        const radius = readBorderRadius(el);
        targetRect = {
          left: rect.left,
          top: rect.top,
          right: rect.right,
          bottom: rect.bottom,
        };
        tourSpotlight.hidden = false;
        tourSpotlight.style.top = `${targetRect.top}px`;
        tourSpotlight.style.left = `${targetRect.left}px`;
        tourSpotlight.style.width = `${rect.width}px`;
        tourSpotlight.style.height = `${rect.height}px`;
        tourSpotlight.style.borderRadius = radius;
        tourSpotlight.style.border = "none";
      }
    }

    requestAnimationFrame(() => {
      requestAnimationFrame(() => placeTourCard(targetRect));
    });
  }

  function renderTourStep() {
    const step = tourSteps[tourIndex];
    const total = tourSteps.length;
    tourStepLabel.textContent = `Passo ${tourIndex + 1} de ${total}`;
    tourTitle.textContent = step.title;
    tourBody.innerHTML = step.body;
    tourProgressBar.style.width = `${((tourIndex + 1) / total) * 100}%`;
    tourPrev.disabled = tourIndex === 0;
    tourNext.textContent = tourIndex === total - 1 ? "Concluir" : "Próximo";
    tourNext.hidden = false;
    positionSpotlight(step.target);
  }

  function startTour() {
    tourActive = true;
    tourIndex = 0;
    if (windowState.main.minimized || windowState.main.closed) restoreWindow("main");
    if (!windowState.options.closed) closeOptions();
    if (!windowState["dialog-create"].closed) closeCreateDialog();
    if (!windowState["dialog-add"].closed) closeAddDialog();
    tourOverlay.classList.remove("hidden");
    tourOverlay.setAttribute("aria-hidden", "false");
    renderTourStep();
  }

  function endTour() {
    tourActive = false;
    tourOverlay.classList.add("hidden");
    tourOverlay.setAttribute("aria-hidden", "true");
    clearTourHighlights();
    localStorage.setItem("anki-prototipo-tour-done", "1");
  }

  document.querySelectorAll("[data-window-controls]").forEach((group) => {
    group.addEventListener("click", (event) => {
      const btn = event.target.closest("[data-win]");
      if (!btn) return;
      event.stopPropagation();
      handleWindowAction(group.getAttribute("data-window-controls"), btn.getAttribute("data-win"));
    });
  });

  document.getElementById("btn-criar-baralho").addEventListener("click", openCreateDialog);
  document.getElementById("dialog-create-cancel").addEventListener("click", closeCreateDialog);
  document.getElementById("overlay-create-backdrop").addEventListener("click", closeCreateDialog);
  document.getElementById("dialog-create-ok").addEventListener("click", createDeck);
  document.getElementById("btn-ajuda").addEventListener("click", startTour);
  document.getElementById("btn-nav-adicionar").addEventListener("click", openAddDialog);
  document.getElementById("overlay-add-backdrop").addEventListener("click", closeAddDialog);
  document.getElementById("btn-add-close").addEventListener("click", closeAddDialog);
  document.getElementById("btn-add-card").addEventListener("click", addCard);
  document.getElementById("btn-add-help").addEventListener("click", () => {
    window.open("https://docs.ankiweb.net/manual/editing", "_blank", "noopener");
  });
  document.getElementById("btn-add-history").addEventListener("click", () => {
    window.alert("Histórico é demonstrativo neste protótipo.");
  });

  document.getElementById("btn-obter-compartilhados").addEventListener("click", () => {
    window.alert(
      "No Anki oficial, esta opção abre a busca de baralhos compartilhados (docs.ankiweb.net, seção Shared Decks)."
    );
  });

  document.getElementById("btn-importar").addEventListener("click", () => {
    window.alert("No Anki oficial, use Arquivo e depois Importar, ou abra um arquivo .apkg.");
  });

  document.querySelectorAll(".menubar__item").forEach((btn) => {
    btn.addEventListener("click", () => {
      if (btn.id === "btn-ajuda") return;
      window.alert(`O menu "${btn.textContent.trim()}" está disponível para interação neste protótipo e permanece demonstrativo.`);
    });
  });

  document.getElementById("add-type-btn").addEventListener("click", () => {
    const typeBtn = document.getElementById("add-type-btn");
    const types = ["Básico", "Básico (e cartão invertido)", "Cloze"];
    const current = typeBtn.textContent.trim();
    const idx = Math.max(0, types.indexOf(current));
    typeBtn.textContent = types[(idx + 1) % types.length];
  });

  document.getElementById("add-deck-btn").addEventListener("click", () => {
    if (!decks.length) return;
    const current = selectedId;
    const idx = Math.max(0, decks.findIndex((d) => d.id === current));
    selectedId = decks[(idx + 1) % decks.length].id;
    syncAddDeckLabel();
    renderDecks();
  });

  document.querySelectorAll(".add-toolbar__text, .add-toolbar__icon").forEach((btn) => {
    btn.addEventListener("click", () => {
      window.alert(`A ferramenta "${btn.textContent.trim() || btn.title}" pode ser usada neste protótipo de forma demonstrativa.`);
    });
  });

  document.querySelectorAll(".preset-select, .select-like").forEach((btn) => {
    btn.addEventListener("click", () => {
      window.alert("Esta lista de opções pode ser aberta e alterada neste protótipo de forma demonstrativa.");
    });
  });

  document.querySelectorAll(".help-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      window.open("https://docs.ankiweb.net/manual/deck-options", "_blank", "noopener");
    });
  });

  document.querySelectorAll(".main-nav__item").forEach((btn) => {
    btn.addEventListener("click", () => {
      const nav = btn.getAttribute("data-nav");
      document.querySelectorAll(".main-nav__item").forEach((el) => el.classList.remove("is-active"));
      btn.classList.add("is-active");
      if (nav === "adicionar") return;
      if (nav === "inicio") {
        if (!windowState.options.closed) closeOptions();
        return;
      }
      if (nav === "painel" || nav === "estatisticas" || nav === "sincronizar") {
        window.alert(`A seção "${btn.textContent.trim()}" está clicável e permanece demonstrativa neste protótipo.`);
      }
    });
  });

  inputDeckName.addEventListener("input", () => {
    btnCreateOk.disabled = inputDeckName.value.trim().length === 0;
  });

  inputDeckName.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !btnCreateOk.disabled) createDeck();
    if (event.key === "Escape") closeCreateDialog();
  });

  addFront.addEventListener("focus", () => {
    addFront.classList.add("is-active");
    addBack.classList.remove("is-active");
  });
  addBack.addEventListener("focus", () => {
    addBack.classList.add("is-active");
    addFront.classList.remove("is-active");
  });

  menuDeck.addEventListener("click", (event) => {
    const item = event.target.closest("[data-action]");
    if (!item) return;
    const action = item.dataset.action;
    if (action === "opcoes") openOptions();
    if (action === "renomear") renameSelected();
    if (action === "excluir") deleteSelected();
    if (action === "exportar") {
      window.alert("Exportar é apenas demonstrativo neste protótipo.");
      closeMenus();
    }
  });

  document.getElementById("btn-save-options").addEventListener("click", closeOptions);
  document.querySelector(".btn-save-chevron")?.addEventListener("click", () => {
    window.alert("As opções adicionais de salvamento estão disponíveis de forma demonstrativa neste protótipo.");
  });

  document.querySelectorAll(".toggle").forEach((toggle) => {
    toggle.addEventListener("click", () => {
      const pressed = toggle.getAttribute("aria-pressed") === "true";
      toggle.setAttribute("aria-pressed", String(!pressed));
    });
  });

  document.querySelectorAll(".scope-tabs").forEach((group) => {
    group.addEventListener("click", (event) => {
      const tab = event.target.closest(".scope-tab");
      if (!tab) return;
      group.querySelectorAll(".scope-tab").forEach((el) => el.classList.remove("is-active"));
      tab.classList.add("is-active");
    });
  });

  document.addEventListener("click", (event) => {
    if (!event.target.closest("#menu-deck") && !event.target.closest("[data-gear]")) {
      closeMenus();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      if (tourActive) endTour();
      else if (!overlayAdd.classList.contains("hidden") && !windowState["dialog-add"].minimized) {
        closeAddDialog();
      } else if (!overlayCreate.classList.contains("hidden") && !windowState["dialog-create"].minimized) {
        closeCreateDialog();
      } else if (!screenOptions.classList.contains("hidden") && !windowState.options.minimized) {
        closeOptions();
      } else closeMenus();
    }
  });

  tourNext.addEventListener("click", () => {
    if (tourIndex >= tourSteps.length - 1) {
      endTour();
      return;
    }
    tourIndex += 1;
    renderTourStep();
  });

  tourPrev.addEventListener("click", () => {
    if (tourIndex === 0) return;
    tourIndex -= 1;
    renderTourStep();
  });

  tourSkip.addEventListener("click", endTour);

  window.addEventListener("resize", () => {
    if (tourActive) positionSpotlight(tourSteps[tourIndex].target);
  });

  app.classList.add("is-maximized");
  updateMaxButtons();
  syncAddDeckLabel();
  renderDecks();
  renderTaskbar();

  if (!localStorage.getItem("anki-prototipo-tour-done")) {
    startTour();
  }
})();
