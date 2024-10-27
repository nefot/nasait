const container = document.querySelector('.carousel-container');
const items = document.querySelectorAll('.carousel-item');
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

let currentIndex = 0;
const itemWidth = items[0].offsetWidth + 20; // 20px — это маржин между элементами

// Клонируем первые и последние карточки для эффекта бесконечной прокрутки
const cloneFirst = items[0].cloneNode(true);
const cloneLast = items[items.length - 1].cloneNode(true);

container.appendChild(cloneFirst);
container.insertBefore(cloneLast, items[0]);

function moveToNext() {
    if (currentIndex >= items.length) {
        container.style.transition = 'none';
        currentIndex = 0;
        container.style.transform = `translateX(-${itemWidth * currentIndex}px)`;
        setTimeout(() => {
            container.style.transition = 'transform 0.5s ease';
            moveToNext();
        }, 50);
    } else {
        currentIndex++;
        container.style.transform = `translateX(-${itemWidth * currentIndex}px)`;
    }
}

function moveToPrev() {
    if (currentIndex <= 0) {
        container.style.transition = 'none';
        currentIndex = items.length - 1;
        container.style.transform = `translateX(-${itemWidth * currentIndex}px)`;
        setTimeout(() => {
            container.style.transition = 'transform 0.5s ease';
            moveToPrev();
        }, 50);
    } else {
        currentIndex--;
        container.style.transform = `translateX(-${itemWidth * currentIndex}px)`;
    }
}

nextButton.addEventListener('click', moveToNext);
prevButton.addEventListener('click', moveToPrev);
