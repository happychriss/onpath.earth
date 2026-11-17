{
  const comparison = document.querySelector('.app-comparison');
  const picker = comparison.querySelector('.comparison-picker');
  const appSelect = picker.querySelector('select');
  const table = comparison.querySelector('.comparison-card');
  const dialog = comparison.querySelector('.comparison-dialog');
  const title = dialog.querySelector('h3');
  const status = dialog.querySelector('.comparison-detail-status');
  const detail = dialog.querySelector('#comparison-detail-text');
  const evidence = dialog.querySelector('.comparison-evidence');
  const source = dialog.querySelector('.comparison-source');
  const extraSource = dialog.querySelector('.comparison-source-extra');
  const preview = comparison.querySelector('.comparison-preview');
  const previewTitle = preview.querySelector('strong');
  const previewStatus = preview.querySelector('.comparison-preview-status');
  const previewDetail = preview.querySelector('p');
  const previewEvidence = preview.querySelector('small');
  let trigger;
  let previewButton;
  let closeTimer;
  let restoringFocus = false;

  function hidePreview() {
    clearTimeout(closeTimer);
    previewButton?.removeAttribute('aria-describedby');
    previewButton = undefined;
    preview.hidden = true;
  }

  function showPreview(button) {
    if (dialog.open || restoringFocus) return;
    hidePreview();
    previewButton = button;
    previewTitle.textContent = button.dataset.title;
    previewStatus.textContent = button.dataset.status || '';
    previewDetail.textContent = button.dataset.detail;
    previewEvidence.textContent = button.dataset.evidence || '';
    previewEvidence.hidden = !button.dataset.evidence;
    preview.hidden = false;
    button.setAttribute('aria-describedby', preview.id);

    positionPreview();
  }

  function positionPreview() {
    if (!previewButton) return;
    const anchor = previewButton.getBoundingClientRect();
    const box = preview.getBoundingClientRect();
    const width = document.documentElement.clientWidth;
    const height = document.documentElement.clientHeight;
    const left = Math.max(12, Math.min(anchor.left + (anchor.width - box.width) / 2, width - box.width - 12));
    const below = anchor.bottom + 5;
    preview.style.left = left + 'px';
    preview.style.top = (below + box.height + 12 <= height ? below : Math.max(12, anchor.top - box.height - 5)) + 'px';
  }

  function deferClose(button) {
    clearTimeout(closeTimer);
    closeTimer = setTimeout(() => {
      if (previewButton === button && !preview.matches(':hover') && !button.matches(':focus-visible')) {
        hidePreview();
      }
    }, 180);
  }

  for (const button of table.querySelectorAll('.comparison-mark')) {
    button.addEventListener('pointerenter', (event) => {
      if (event.pointerType === 'mouse' && window.matchMedia('(any-hover: hover)').matches) showPreview(button);
    });
    button.addEventListener('pointerleave', () => deferClose(button));
    button.addEventListener('focus', () => {
      if (button.matches(':focus-visible')) showPreview(button);
    });
    button.addEventListener('blur', () => {
      if (previewButton === button && !button.matches(':hover') && !preview.matches(':hover')) hidePreview();
    });
  }
  preview.addEventListener('pointerenter', () => clearTimeout(closeTimer));
  preview.addEventListener('pointerleave', () => {
    if (previewButton) deferClose(previewButton);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && previewButton) hidePreview();
  });
  window.addEventListener('scroll', (event) => {
    if (!previewButton || event.target === preview) return;
    if (previewButton.matches(':focus-visible')) positionPreview();
    else hidePreview();
  }, { passive: true, capture: true });
  window.addEventListener('resize', hidePreview);

  const updateSelectedApp = () => {
    hidePreview();
    table.dataset.app = appSelect.value;
  };
  updateSelectedApp();
  appSelect.addEventListener('change', updateSelectedApp);
  table.dataset.enhanced = '';
  picker.hidden = false;

  comparison.addEventListener('click', (event) => {
    const button = event.target.closest('.comparison-mark');
    if (!button) return;

    hidePreview();
    trigger = button;
    title.textContent = button.dataset.title;
    status.textContent = button.dataset.status || '';
    detail.textContent = button.dataset.detail;
    evidence.textContent = button.dataset.evidence || '';
    evidence.hidden = !button.dataset.evidence;
    source.hidden = !button.dataset.source;
    source.href = button.dataset.source || '#';
    extraSource.hidden = !button.dataset.sourceExtra;
    extraSource.href = button.dataset.sourceExtra || '#';
    dialog.showModal();
  });

  dialog.addEventListener('close', () => {
    restoringFocus = true;
    trigger.focus();
    restoringFocus = false;
    hidePreview();
  });
}
