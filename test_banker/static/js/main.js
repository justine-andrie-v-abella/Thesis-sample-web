// Common JavaScript functions used across all pages

// Sidebar toggle functionality
function setupSidebarToggle(sidebarId, mainContentId, toggleButtonId) {
    const toggleButton = document.getElementById(toggleButtonId);
    const sidebar = document.getElementById(sidebarId);
    const mainContent = document.getElementById(mainContentId);
    
    if (toggleButton && sidebar) {
        toggleButton.addEventListener('click', function() {
            if (window.innerWidth < 1024) {
                // Mobile behavior - toggle overlay sidebar
                const isOpening = !sidebar.classList.contains('mobile-open');
                sidebar.classList.toggle('mobile-open');
                
                // Add overlay to main content when sidebar is open
                if (mainContent) {
                    if (isOpening) {
                        mainContent.classList.add('mobile-overlay');
                        document.body.style.overflow = 'hidden';
                    } else {
                        mainContent.classList.remove('mobile-overlay');
                        document.body.style.overflow = '';
                    }
                }
            } else {
                // Desktop behavior - toggle collapsed state
                sidebar.classList.toggle('collapsed');
            }
        });
    }
}

// Inner sidebar toggle (the three lines inside sidebar)
function setupInnerSidebarToggle() {
    const innerToggle = document.getElementById('sidebar-toggle-inner');
    const sidebar = document.getElementById('sidebar');
    
    if (innerToggle && sidebar) {
        innerToggle.addEventListener('click', function() {
            if (window.innerWidth >= 1024) {
                // Only toggle on desktop
                sidebar.classList.toggle('collapsed');
            }
        });
    }
}

// Close sidebar when clicking on overlay (mobile/tablet)
function setupMobileOverlayClose(sidebarId, mainContentId) {
    const sidebar = document.getElementById(sidebarId);
    const mainContent = document.getElementById(mainContentId);
    
    if (mainContent) {
        mainContent.addEventListener('click', function(e) {
            if (window.innerWidth < 1024 && 
                sidebar && 
                sidebar.classList.contains('mobile-open') &&
                !e.target.closest('#' + sidebarId)) {
                closeMobileSidebar(sidebar, mainContent);
            }
        });
    }
}

// Close mobile sidebar
function closeMobileSidebar(sidebar, mainContent) {
    sidebar.classList.remove('mobile-open');
    if (mainContent) {
        mainContent.classList.remove('mobile-overlay');
    }
    document.body.style.overflow = '';
}

// Handle window resize
function handleResize() {
    const sidebar = document.getElementById('sidebar') || document.getElementById('teacher-sidebar');
    const mainContent = document.getElementById('main-content') || document.getElementById('teacher-main-content');
    
    if (window.innerWidth >= 1024) {
        // Desktop - ensure sidebar is visible and reset mobile states
        if (sidebar) {
            sidebar.classList.remove('mobile-open');
        }
        if (mainContent) {
            mainContent.classList.remove('mobile-overlay');
            document.body.style.overflow = '';
        }
    } else {
        // Mobile - ensure sidebar is hidden and reset collapsed state
        if (sidebar) {
            sidebar.classList.remove('collapsed');
            sidebar.classList.remove('mobile-open');
        }
        if (mainContent) {
            mainContent.classList.remove('mobile-overlay');
            document.body.style.overflow = '';
        }
    }
}

// Initialize common functionality when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Setup sidebar toggles
    setupSidebarToggle('sidebar', 'main-content', 'sidebar-toggle');
    setupSidebarToggle('teacher-sidebar', 'teacher-main-content', 'teacher-sidebar-toggle');
    
    // Setup inner sidebar toggle
    setupInnerSidebarToggle();
    
    // Setup mobile overlay close
    setupMobileOverlayClose('sidebar', 'main-content');
    setupMobileOverlayClose('teacher-sidebar', 'teacher-main-content');
    
    // Handle window resize
    window.addEventListener('resize', handleResize);
    handleResize(); // Initial call
    
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
});