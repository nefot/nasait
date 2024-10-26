// Обновляем ссылки на элементы
const container = document.querySelector('.carousel-inner');
let items = document.querySelectorAll('.carousel-item');
const prevButton = document.querySelector('.carousel-control-prev');
const nextButton = document.querySelector('.carousel-control-next');

let currentIndex = 1;
const itemWidth = items[0].offsetWidth + 20; // Учитываем отступ

// Клонируем первые и последние элементы
const cloneFirst = items[0].cloneNode(true);
const cloneLast = items[items.length - 1].cloneNode(true);
container.appendChild(cloneFirst);
container.insertBefore(cloneLast, items[0]);

// Обновляем список элементов для учета клонов
items = document.querySelectorAll('.carousel-item');
container.style.transform = `translateX(-${itemWidth * currentIndex}px)`;

function moveToNext() {
    currentIndex++;
    container.style.transition = 'transform 0.5s ease';
    container.style.transform = `translateX(-${itemWidth * currentIndex}px)`;

    if (currentIndex >= items.length - 1) {
        setTimeout(() => {
            container.style.transition = 'none';
            currentIndex = 1;
            container.style.transform = `translateX(-${itemWidth * currentIndex}px)`;
        }, 500);
    }
}

function moveToPrev() {
    currentIndex--;
    container.style.transition = 'transform 0.5s ease';
    container.style.transform = `translateX(-${itemWidth * currentIndex}px)`;

    if (currentIndex <= 0) {
        setTimeout(() => {
            container.style.transition = 'none';
            currentIndex = items.length - 2;
            container.style.transform = `translateX(-${itemWidth * currentIndex}px)`;
        }, 500);
    }
}

nextButton.addEventListener('click', moveToNext);
prevButton.addEventListener('click', moveToPrev);
