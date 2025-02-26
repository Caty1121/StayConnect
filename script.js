document.addEventListener('DOMContentLoaded', function() {
  console.log("DOM fully loaded and parsed");

  // Modal elements
  const modals = {
      register: document.getElementById('registerModal'),
      password: document.getElementById('passwordModal')
  };

  const registerLink = document.getElementById('register'); 

  // Buttons to open modals
  const openModalBtns = {
      register: document.getElementById('openModal'),
      password: document.getElementById('forgot-password') // Forgot password link
  };

  // Close buttons
  const closeBtns = document.querySelectorAll('.close');
  const closeModalFinalBtns = document.querySelectorAll('#closeModal');

  // Form steps
  const steps = document.querySelectorAll('.form-step'); // Registration steps
  const passwordSteps = document.querySelectorAll('.form-step-2'); // Password reset steps
  const confirmDetailsDiv = document.getElementById('confirm-pw'); // Confirmation div

  let currentStep = {
      register: 1,
      password: 1
  };

  function showStep(modalType, step) {
      const stepsGroup = modalType === 'register' ? steps : passwordSteps;
      stepsGroup.forEach((stepElement, index) => {
          stepElement.classList.toggle('active', index + 1 === step);
      });
      currentStep[modalType] = step;
  }

  // Open modal function
  function openModal(modalType) {
      modals[modalType].style.display = 'flex';
      showStep(modalType, 1); // Start at the first step
      if (modalType === 'password') {
        confirmDetailsDiv.style.display = 'none'; // Ensure it's hidden when modal opens
    }
  }

  // Close modal function
  function closeModal(modalType) {
      modals[modalType].style.display = 'none';
  }

  // Event listeners for opening modals
  openModalBtns.register.addEventListener('click', () => openModal('register'));
  openModalBtns.password.addEventListener('click', () => openModal('password'));

  registerLink.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent default link behavior
    openModal('register');
});

  // Event listeners for closing modals
  closeBtns.forEach(btn => {
      btn.addEventListener('click', () => {
          Object.keys(modals).forEach(modal => closeModal(modal));
      });
  });

  closeModalFinalBtns.forEach(btn => {
      btn.addEventListener('click', () => {
          Object.keys(modals).forEach(modal => closeModal(modal));
      });
  });

  // Navigation for Registration Modal
  document.getElementById('nextStep1').addEventListener('click', () => showStep('register', 2));
  document.getElementById('prevStep2').addEventListener('click', () => showStep('register', 1));
  document.getElementById('nextStep2').addEventListener('click', () => showStep('register', 3));

  // Navigation for Forgot Password Modal
  document.getElementById('pwNextStep1').addEventListener('click', () => showStep('password', 2));
  document.getElementById('pwPrevStep2').addEventListener('click', () => showStep('password', 1));

  // Handle clicking outside the modal to close it
  window.addEventListener('click', (event) => {
      Object.keys(modals).forEach(modal => {
          if (event.target === modals[modal]) {
              closeModal(modal);
          }
      });
  });

  document.getElementById('pwResetSubmit').addEventListener('click', () => {
    console.log("Submit button clicked. Showing confirmation message.");

    // Hide Step 2 and Show Confirming Details
    document.getElementById('password-step2').classList.remove('active');
    document.getElementById('password-step2').style.display = 'none'; // Ensures step 2 disappears

    confirmDetailsDiv.style.display = 'block'; // Ensures confirmation message appears
});


  console.log("Event listeners set up successfully.");
});
