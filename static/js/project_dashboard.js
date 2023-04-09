const options = {
    modules: {
        // imageResize: {
        //     displaySize: true
        //   },
        toolbar: [
          [{ header: [1, 2, 3, 4, 5, 6,  false] }],
          ['bold', 'italic', 'underline','strike'],
          ['image', 'code-block'],
          ['link'],
          [{ 'script': 'sub'}, { 'script': 'super' }],
          [{ 'list': 'ordered'}, { 'list': 'bullet' }],
          ['clean']
        ]
      },
theme: "snow",
enable: false
};
var projectBody = document.getElementById('project-body'),
projectContainer = document.getElementById('project-container'),
    editButton = document.getElementById('edit-project-description'),
    cancelButton = document.getElementById('cancel-project-description');

var quill = new Quill(projectBody, options);
projectContainer.classList.add('inactive');
quill.enable(false);
$("#save-project-description").attr("style", "display:none");
$("#cancel-project-description").attr("style", "display:none");

$("#edit-project-description").click(function (e) {
    projectContainer.classList.remove('inactive');
    quill.enable(true);
    $("#edit-project-description").attr("style", "display:none");
    $("#save-project-description").attr("style", "display:inline-block");
    $("#cancel-project-description").attr("style", "display:inline-block");
});

$("#cancel-project-description").click(function (e) {
    projectContainer.classList.add('inactive');
    quill.enable(false);
    $("#edit-project-description").attr("style", "display:inline-block");
    $("#save-project-description").attr("style", "display:none");
    $("#cancel-project-description").attr("style", "display:none");
});

$("#save-project-description").click(function (e) {
    e.preventDefault();
    var project_description = quill.root.innerHTML;
    var project_id = document.getElementById('project-id').innerHTML;
    $.ajax({
        type: "POST",
        url: "/save_project_description",
        data: JSON.stringify(
            { "project_id": project_id,
                "project_description" : project_description 
            }),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
            projectContainer.classList.add('inactive');
            quill.enable(false);
            $("#edit-project-description").attr("style", "display:block");
            $("#save-project-description").attr("style", "display:none");
            $("#cancel-project-description").attr("style", "display:none");
            $("#project-container").innerHTML = JSON.stringify(data);
        }
    });

});