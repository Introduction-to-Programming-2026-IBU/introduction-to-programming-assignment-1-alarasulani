/**
 * Exercise 6: Fetch & APIs
 */

// ============================================================
// UTILITY: Show a loading spinner inside an element
// ============================================================
function showLoading(element) {
  element.innerHTML = '<div class="spinner"></div>';
}

function showError(element, message) {
  element.innerHTML = `<p class="error-text">❌ ${message}</p>`;
}


// ============================================================
// TASK 1 — Random Quote
// ============================================================
const quoteDisplay = document.querySelector('#quote-display');
const btnNewQuote  = document.querySelector('#btn-new-quote');

async function fetchQuote() {
  showLoading(quoteDisplay);

  try {
    const response = await fetch('https://api.quotable.io/random');
    if (!response.ok) throw new Error('Network response was not ok');
    
    const data = await response.json();
    
    quoteDisplay.innerHTML = `
      <blockquote>"${data.content}"</blockquote>
      <p class="quote-author">— ${data.author}</p>
    `;

  } catch (error) {
    showError(quoteDisplay, 'Could not load quote. Check your connection.');
    console.error(error);
  }
}

fetchQuote();
btnNewQuote.addEventListener('click', fetchQuote);


// ============================================================
// TASK 2 — GitHub User Search
// ============================================================
const githubInput  = document.querySelector('#github-input');
const btnSearch    = document.querySelector('#btn-search-user');
const githubResult = document.querySelector('#github-result');

async function searchUser() {
  const username = githubInput.value.trim();
  if (!username) return;

  showLoading(githubResult);

  try {
    const response = await fetch(`https://api.github.com/users/${username}`);
    
    if (response.status === 404) {
      showError(githubResult, 'User not found');
      return;
    }
    
    if (!response.ok) throw new Error('Search failed');

    const data = await response.json();
    
    githubResult.innerHTML = `
      <div class="github-profile">
        <img src="${data.avatar_url}" alt="${data.login}" width="100">
        <h3>${data.name || data.login}</h3>
        <p>${data.bio || 'No bio available'}</p>
        <ul>
          <li>Followers: ${data.followers}</li>
          <li>Public Repos: ${data.public_repos}</li>
        </ul>
        <a href="${data.html_url}" target="_blank">View Profile</a>
      </div>
    `;

  } catch (error) {
    showError(githubResult, error.message || 'Search failed. Try again.');
  }
}

btnSearch.addEventListener('click', searchUser);
githubInput.addEventListener('keydown', (e) => { if (e.key === 'Enter') searchUser(); });


// ============================================================
// TASK 3 — Posts Feed with Pagination
// ============================================================
const postsContainer = document.querySelector('#posts-container');
const btnLoadMore    = document.querySelector('#btn-load-more');
let currentPage = 1;
const postsPerPage = 10;

async function loadPosts() {
  const start = (currentPage - 1) * postsPerPage;
  
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/posts?_start=${start}&_limit=${postsPerPage}`);
    const posts = await response.json();

    posts.forEach(post => {
      const card = document.createElement('div');
      card.className = 'post-card';
      card.innerHTML = `
        <h3>${post.title}</h3>
        <p>${post.body}</p>
        <div class="comments-section" id="comments-${post.id}"></div>
      `;
      card.addEventListener('click', () => loadComments(post.id, card));
      postsContainer.appendChild(card);
    });

    currentPage++;
  } catch (error) {
    console.error("Posts could not be loaded", error);
  }
}

async function loadComments(postId, cardElement) {
  const commentDiv = cardElement.querySelector('.comments-section');
  
  if (commentDiv.innerHTML !== "") {
    commentDiv.innerHTML = ""; // Toggle: Varsa temizle (gizle)
    return;
  }

  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}/comments`);
    const comments = await response.json();
    
    commentDiv.innerHTML = '<h4>Comments:</h4>' + comments.map(c => `
      <div class="comment">
        <p><strong>${c.email}:</strong> ${c.body}</p>
      </div>
    `).join('');
  } catch (error) {
    console.error("Comments could not be loaded", error);
  }
}

loadPosts();
btnLoadMore.addEventListener('click', loadPosts);


// ============================================================
// TASK 5 — Promise.all: Parallel Fetches
// ============================================================
const btnFetchAll  = document.querySelector('#btn-fetch-all');
const multiResult  = document.querySelector('#multi-result');

async function fetchAllParallel() {
  showLoading(multiResult);

  try {
    const [quoteRes, userRes, todoRes] = await Promise.all([
      fetch('https://api.quotable.io/random'),
      fetch('https://jsonplaceholder.typicode.com/users/1'),
      fetch('https://jsonplaceholder.typicode.com/todos/1')
    ]);

    const [quote, user, todo] = await Promise.all([
      quoteRes.json(), userRes.json(), todoRes.json()
    ]);

    multiResult.innerHTML = `
      <div class="multi-fetch-box">
        <p><strong>Quote:</strong> ${quote.content}</p>
        <p><strong>User:</strong> ${user.name}</p>
        <p><strong>Todo:</strong> ${todo.title} (${todo.completed ? '✅' : '❌'})</p>
      </div>
    `;

  } catch (error) {
    showError(multiResult, 'One or more requests failed.');
  }
}

btnFetchAll.addEventListener('click', fetchAllParallel);