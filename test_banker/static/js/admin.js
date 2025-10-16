// Admin-specific JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Setup admin sidebar toggle
    setupSidebarToggle('sidebar', 'main-content', 'sidebar-toggle');
    
    // Setup all modals
    setupModal('create-department-modal', 'create-department-btn', 'close-department-modal');
    setupModal('create-subject-modal', 'create-subject-btn', 'close-subject-modal');
    setupModal('create-teacher-modal', 'create-teacher-btn', 'close-teacher-modal');
    setupModal('create-folder-modal', 'create-folder-btn', 'close-folder-modal');
    
    // File actions
    document.querySelectorAll('.view-file').forEach(button => {
        button.addEventListener('click', function() {
            const fileId = this.getAttribute('data-file-id');
            console.log('View file:', fileId);
        });
    });
    
    document.querySelectorAll('.download-file').forEach(button => {
        button.addEventListener('click', function() {
            const fileId = this.getAttribute('data-file-id');
            console.log('Download file:', fileId);
        });
    });
    
    document.querySelectorAll('.delete-file').forEach(button => {
        button.addEventListener('click', function() {
            const fileId = this.getAttribute('data-file-id');
            if (confirm('Are you sure you want to delete this file?')) {
                console.log('Delete file:', fileId);
            }
        });
    });
    
    // Form submissions
    const forms = ['create-department-form', 'create-subject-form', 'create-teacher-form', 'create-folder-form'];
    forms.forEach(formId => {
        const form = document.getElementById(formId);
        if (form) {
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                // Handle form submission
                console.log('Form submitted:', formId);
                // Close modal after submission
                const modal = this.closest('.modal');
                if (modal) {
                    modal.classList.remove('active');
                }
            });
        }
    });
});