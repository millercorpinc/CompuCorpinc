document.addEventListener('DOMContentLoaded', () => {
  const yearNode = document.createElement('span');
  yearNode.textContent = new Date().getFullYear();
  const footerText = document.querySelector('.site-footer p');
  if (footerText) {
    footerText.textContent = `Internal operating presentation · ${yearNode.textContent} · Not for external distribution`;
  }
});
