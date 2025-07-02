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

  // お問い合わせフォーム送信処理
  const contactForm = document.getElementById("contact-form");
  if (contactForm) {
    contactForm.addEventListener("submit", handleFormSubmit);
  }
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

// フォーム送信処理
async function handleFormSubmit(e) {
  e.preventDefault();
  
  const form = e.target;
  const submitButton = form.querySelector('button[type="submit"]');
  const submitText = submitButton.querySelector('.submit-text');
  const loadingText = submitButton.querySelector('.loading-text');
  
  // ボタンを送信中状態に変更
  submitButton.disabled = true;
  submitText.classList.add('hidden');
  loadingText.classList.remove('hidden');
  
  try {
    const formData = new FormData(form);
    
    const response = await fetch('send_mail.php', {
      method: 'POST',
      body: formData
    });
    
    const result = await response.json();
    
    if (result.success) {
      // 成功時の処理
      form.reset();
      showSuccessPopup(result.message);
    } else {
      // エラー時の処理
      showErrorPopup(result.message);
    }
    
  } catch (error) {
    console.error('フォーム送信エラー:', error);
    showErrorPopup('送信に失敗しました。お手数ですが、お電話（070-4080-0965）にてお問い合わせください。');
  } finally {
    // ボタンを元の状態に戻す
    submitButton.disabled = false;
    submitText.classList.remove('hidden');
    loadingText.classList.add('hidden');
  }
}

// 成功ポップアップを表示
function showSuccessPopup(message) {
  const popup = document.getElementById('success-popup');
  const messageElement = document.getElementById('success-message');
  messageElement.textContent = message;
  popup.classList.remove('hidden');
  
  // ページの最上部にスクロール
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// エラーポップアップを表示
function showErrorPopup(message) {
  const popup = document.getElementById('error-popup');
  const messageElement = document.getElementById('error-message');
  messageElement.textContent = message;
  popup.classList.remove('hidden');
}

// 成功ポップアップを閉じる
function closeSuccessPopup() {
  const popup = document.getElementById('success-popup');
  popup.classList.add('hidden');
}

// エラーポップアップを閉じる
function closeErrorPopup() {
  const popup = document.getElementById('error-popup');
  popup.classList.add('hidden');
}

// ポップアップの背景クリックで閉じる
document.addEventListener('click', function(e) {
  if (e.target.id === 'success-popup') {
    closeSuccessPopup();
  }
  if (e.target.id === 'error-popup') {
    closeErrorPopup();
  }
});

// ESCキーでポップアップを閉じる
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    closeSuccessPopup();
    closeErrorPopup();
  }
});