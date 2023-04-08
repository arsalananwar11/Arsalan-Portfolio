const options = {
theme: "snow",
enable: false
};
var projectBody = document.getElementById('project-body'),
projectContainer = document.getElementById('project-container'),
    onButton = document.getElementById('on'),
    offButton = document.getElementById('off');

var quill = new Quill(projectBody, options);

onButton.addEventListener('click', function() {
projectContainer.classList.remove('inactive')
quill.enable(true);
});

offButton.addEventListener('click', function() {
projectContainer.classList.add('inactive');
quill.enable(false);
}); 