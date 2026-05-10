/**
 * Exercise 5: Forms & Validation
 */

const form = document.querySelector('#registration-form');

// ============================================================
// HELPER: Show or clear an error on a field
// ============================================================
function showError(inputId, message) {
  const input = document.querySelector(`#${inputId}`);
  const errorSpan = document.querySelector(`#error-${inputId}`);
  input.classList.add('invalid');
  input.classList.remove('valid');
  errorSpan.textContent = message;
}

function clearError(inputId) {
  const input = document.querySelector(`#${inputId}`);
  const errorSpan = document.querySelector(`#error-${inputId}`);
  input.classList.remove('invalid');
  input.classList.add('valid');
  errorSpan.textContent = "";
}

// ============================================================
// TASK 2: Individual Field Validators
// ============================================================

function validateName() {
  const value = document.querySelector('#full-name').value.trim();
  if (value.length < 2) {
    showError('full-name', 'Name must be at least 2 characters.');
    return false;
  }
  clearError('full-name');
  return true;
}

function validateEmail() {
  const value = document.querySelector('#email').value.trim();
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!regex.test(value)) {
    showError('email', 'Please enter a valid email address.');
    return false;
  }
  clearError('email');
  return true;
}

function validatePassword() {
  const value = document.querySelector('#password').value;
  const hasDigit = /\d/.test(value);
  if (value.length < 8 || !hasDigit) {
    showError('password', 'Must be 8+ characters and contain at least one digit.');
    return false;
  }
  clearError('password');
  return true;
}

function validateConfirmPassword() {
  const pass = document.querySelector('#password').value;
  const confirm = document.querySelector('#confirm-password').value;
  if (confirm !== pass || confirm === "") {
    showError('confirm-password', 'Passwords do not match.');
    return false;
  }
  clearError('confirm-password');
  return true;
}

function validateAge() {
  const birthDateValue = document.querySelector('#birth-date').value;
  if (!birthDateValue) {
    showError('birth-date', 'Please select your birth date.');
    return false;
  }
  
  const birthDate = new Date(birthDateValue);
  const today = new Date();
  let age = today.getFullYear() - birthDate.getFullYear();
  const m = today.getMonth() - birthDate.getMonth();
  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }

  if (age < 18 || age > 120) {
    showError('birth-date', 'You must be between 18 and 120 years old.');
    return false;
  }
  clearError('birth-date');
  return true;
}

function validateGender() {
  const value = document.querySelector('#gender').value;
  if (value === "") {
    showError('gender', 'Please select your gender.');
    return false;
  }
  clearError('gender');
  return true;
}

function validateTerms() {
  const checkbox = document.querySelector('#terms');
  if (!checkbox.checked) {
    showError('terms', 'You must agree to the terms.');
    return false;
  }
  clearError('terms');
  return true;
}

// ============================================================
// TASK 5: Bio Character Counter
// ============================================================
const bioTextarea = document.querySelector('#bio');
const submitBtn = document.querySelector('#submit-btn');

bioTextarea.addEventListener('input', function() {
  const length = bioTextarea.value.length;
  // Not: HTML'e bir karakter sayacı eklemediysen hata vermemesi için kontrol ekliyoruz
  const charCounter = document.querySelector('#char-count'); 
  if (charCounter) {
    charCounter.textContent = `${length} / 200 characters`;
    if (length > 200) {
      charCounter.classList.add('over-limit');
      submitBtn.disabled = true;
    } else {
      charCounter.classList.remove('over-limit');
      submitBtn.disabled = false;
    }
  }
});

// ============================================================
// TASK 2: Attach real-time listeners
// ============================================================
document.querySelector('#full-name').addEventListener('blur', validateName);
document.querySelector('#email').addEventListener('blur', validateEmail);
document.querySelector('#password').addEventListener('input', validatePassword);
document.querySelector('#confirm-password').addEventListener('input', validateConfirmPassword);
document.querySelector('#birth-date').addEventListener('blur', validateAge);
document.querySelector('#gender').addEventListener('change', validateGender);
document.querySelector('#terms').addEventListener('change', validateTerms);

// ============================================================
// TASK 3: Submit Handler
// ============================================================
form.addEventListener('submit', function(event) {
  event.preventDefault();

  const isNameValid = validateName();
  const isEmailValid = validateEmail();
  const isPasswordValid = validatePassword();
  const isConfirmValid = validateConfirmPassword();
  const isAgeValid = validateAge();
  const isGenderValid = validateGender();
  const isTermsValid = validateTerms();

  if (isNameValid && isEmailValid && isPasswordValid && isConfirmValid && isAgeValid && isGenderValid && isTermsValid) {
    document.querySelector('#success-message').classList.remove('hidden');
    form.classList.add('hidden');
    window.scrollTo(0, 0);
  } else {
    // İlk hatalı alana odaklan
    const firstInvalid = document.querySelector('.invalid');
    if (firstInvalid) firstInvalid.focus();
  }
});