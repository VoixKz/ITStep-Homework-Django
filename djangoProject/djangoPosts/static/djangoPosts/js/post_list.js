const searchInput = document.getElementById('searchInput');
const genreSelect = document.getElementById('genreSelect');
const postGrid = document.getElementById('postGrid');
const posts = postGrid.getElementsByClassName('post_item');

function filterPosts() {
    const filter = searchInput.value.toLowerCase();
    const selectedGenre = genreSelect.value.toLowerCase();

    Array.from(posts).forEach(post => {
        const title = post.querySelector('.post-title').textContent.toLowerCase();
        const subtitle = post.querySelector('.post-subtitle').textContent.toLowerCase();
        const genre = post.querySelector('.post-genre').textContent.toLowerCase();

        const matchesFilter = title.includes(filter) || subtitle.includes(filter);
        const matchesGenre = !selectedGenre || genre === selectedGenre;

        if (matchesFilter && matchesGenre) {
            post.style.display = '';
        } else {
            post.style.display = 'none';
        }
    });
}

searchInput.addEventListener('input', filterPosts);
genreSelect.addEventListener('change', filterPosts);