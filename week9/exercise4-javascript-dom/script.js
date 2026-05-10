/**
 * Exercise 4: JavaScript & the DOM
 */

// ============================================================
// TASK 1 — Console Warmup
// ============================================================

// TODO 1a: Başlığı değiştir
const mainTitle = document.querySelector('#main-title');
mainTitle.textContent = "DOM Mastery 🚀";

// TODO 1b: Tüm kartları seç ve sayısını logla
const allCards = document.querySelectorAll('.card');
console.log("Toplam kart sayısı:", allCards.length);

// TODO 1c: Target box rengini değiştir
const targetBox = document.querySelector('#target-box');
targetBox.style.backgroundColor = "#e8a838";


// ============================================================
// TASK 2 — Click Counter
// ============================================================

const countDisplay = document.querySelector('#count-display');
const btnIncrement = document.querySelector('#btn-increment');
const btnDecrement = document.querySelector('#btn-decrement');
const btnReset = document.querySelector('#btn-reset');

let count = 0;

function updateCountDisplay() {
  countDisplay.textContent = count;
  
  // Renk sınıflarını ayarla
  if (count === 0) {
    countDisplay.classList.add('zero');
    countDisplay.classList.remove('high');
  } else if (count > 5) {
    countDisplay.classList.add('high');
    countDisplay.classList.remove('zero');
  } else {
    countDisplay.classList.remove('zero', 'high');
  }
}

btnIncrement.addEventListener('click', () => {
  count++;
  updateCountDisplay();
});

btnDecrement.addEventListener('click', () => {
  if (count > 0) {
    count--;
    updateCountDisplay();
  }
});

btnReset.addEventListener('click', () => {
  count = 0;
  updateCountDisplay();
});

updateCountDisplay();


// ============================================================
// TASK 3 — Dynamic List Builder
// ============================================================

const listInput = document.querySelector('#list-input');
const dynamicList = document.querySelector('#dynamic-list');
const btnAddItem = document.querySelector('#btn-add-item');

btnAddItem.addEventListener('click', () => {
  const text = listInput.value.trim();
  
  if (text === "") {
    alert("Lütfen bir şeyler yazın!");
    return;
  }

  const li = document.createElement('li');
  li.innerHTML = `${text} <button class="delete-btn">×</button>`;
  dynamicList.appendChild(li);
  
  listInput.value = "";
  listInput.focus();
});

// Silme işlemi (Event Delegation)
dynamicList.addEventListener('click', function(event) {
  if (event.target.classList.contains('delete-btn')) {
    event.target.parentElement.remove();
  }
});


// ============================================================
// TASK 4 — Show / Hide Toggle
// ============================================================

const toggleBtn = document.querySelector('#btn-toggle');
const detailsDiv = document.querySelector('.details');

toggleBtn.addEventListener('click', () => {
  detailsDiv.classList.toggle('hidden');
  
  if (detailsDiv.classList.contains('hidden')) {
    toggleBtn.textContent = "Show Details";
  } else {
    toggleBtn.textContent = "Hide Details";
  }
});


// ============================================================
// TASK 5 — Color Mixer
// ============================================================

const sliderR = document.querySelector('#slider-r');
const sliderG = document.querySelector('#slider-g');
const sliderB = document.querySelector('#slider-b');
const colorPreview = document.querySelector('#color-preview');
const hexDisplay = document.querySelector('#hex-display');

const valR = document.querySelector('#val-r');
const valG = document.querySelector('#val-g');
const valB = document.querySelector('#val-b');

function updateColor() {
  const r = parseInt(sliderR.value);
  const g = parseInt(sliderG.value);
  const b = parseInt(sliderB.value);

  // Sayıları güncelle
  valR.textContent = r;
  valG.textContent = g;
  valB.textContent = b;

  // Kutunun rengini güncelle
  colorPreview.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;

  // Hex kodunu hesapla
  const hex = "#" + [r, g, b].map(x => x.toString(16).padStart(2, '0')).join('');
  hexDisplay.textContent = hex.toUpperCase();
}

sliderR.addEventListener('input', updateColor);
sliderG.addEventListener('input', updateColor);
sliderB.addEventListener('input', updateColor);

updateColor();