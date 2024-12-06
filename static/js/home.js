document.addEventListener('DOMContentLoaded', function () {
    fetch("/announcements")
        .then(response => response.json())
        .then(data => {
            var announcements = data.announcements;
            if (Array.isArray(announcements)) {
                var announcementIndex = 0;
                var announcementElement = document.getElementById("announcement");

                function updateAnnouncement() {
                    announcementElement.classList.remove("active");
                    setTimeout(() => {
                        announcementElement.innerText = announcements[announcementIndex];
                        announcementElement.classList.add("active");
                        announcementIndex = (announcementIndex + 1) % announcements.length;
                    }, 500);
                }

                setInterval(updateAnnouncement, 5000);
                updateAnnouncement();
            }
        })
        .catch(error => { alert("Error: " + error); });

});