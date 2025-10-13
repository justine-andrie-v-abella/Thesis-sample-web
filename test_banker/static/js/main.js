// Common JavaScript functions
function setupSidebarToggle(sidebarId, mainContentId, toggleButtonId) {
    const toggleButton = document.getElementById(toggleButtonId);
    if (toggleButton) {
        toggleButton.addEventListener('click', function() {
            const sidebar = document.getElementById(sidebarId);
            const mainContent = document.getElementById(mainContentId);
            
            sidebar.classList.toggle('collapsed');
            if (mainContent) {
                mainContent.classList.toggle('ml-64');
                mainContent.classList.toggle('ml-16');
            }
        });
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Setup sidebar toggles
    setupSidebarToggle('sidebar', 'main-content', 'sidebar-toggle');
    setupSidebarToggle('teacher-sidebar', 'teacher-main-content', 'teacher-sidebar-toggle');
});