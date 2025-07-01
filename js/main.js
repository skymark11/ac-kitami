document.addEventListener("DOMContentLoaded", function () {
  // モバイルメニュー開閉
  const mobileMenuButton = document.getElementById("mobile-menu-button");
  const mobileMenu = document.getElementById("mobile-menu");
  mobileMenuButton.addEventListener("click", function () {
    mobileMenu.classList.toggle("hidden");
  });
  // メニュー項目クリックで閉じる
  mobileMenu.querySelectorAll("a").forEach(item => {
    item.addEventListener("click", () => {
      mobileMenu.classList.add("hidden");
    });
  });

  // FAQ アコーディオン
  document.querySelectorAll(".faq-button").forEach(button => {
    button.addEventListener("click", function () {
      const target = document.getElementById(this.dataset.target);
      const icon = this.querySelector(".faq-icon");
      const isHidden = target.classList.toggle("hidden");
      icon.classList.toggle("ri-add-line", !isHidden);
      icon.classList.toggle("ri-subtract-line", isHidden);
    });
  });
});
// スムーズスクロール機能
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      const headerOffset = 80; // ヘッダーの高さ分のオフセット
      const elementPosition = target.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  });
});
