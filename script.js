document.addEventListener('DOMContentLoaded', function() {
  console.log("DOM fully loaded and parsed");
  const modal = document.getElementById('registerModal');
  const openModalBtn = document.getElementById('openModal');
  const regLink = document.getElementById('reg-link');
  const closeModalBtn = document.getElementById('closeModal');
  const close = document.getElementById('close');
  const steps = document.querySelectorAll('.form-step');
  const nextStep1Btn = document.getElementById('nextStep1');
  const prevStep2Btn = document.getElementById('prevStep2');
  const nextStep2Btn = document.getElementById('nextStep2');

  console.log("Elements selected:", { modal, openModalBtn, closeModalBtn, steps, nextStep1Btn, prevStep2Btn, nextStep2Btn });

  let currentStep = 1;

  function showStep(step) {
    console.log("Showing step:", step);
      steps.forEach((stepElement, index) => {
          if (index + 1 === step) {
              stepElement.classList.add('active');
          } else {
              stepElement.classList.remove('active');
          }
      });
  }

  openModalBtn.addEventListener('click', () => {
    console.log("Open modal button clicked");
      modal.style.display = 'flex';
      console.log("Modal display property:", modal.style.display);
      showStep(1);
  });

  regLink.addEventListener('click', () => {
    console.log("Open modal reg-link clicked");
      modal.style.display = 'flex';
      console.log("Modal display property:", modal.style.display);
      showStep(1);
  });

  closeModalBtn.addEventListener('click', () => {
    console.log("Close modal button clicked");
    modal.style.display = 'none';
  });
  
  close.addEventListener('click', () => {
    console.log("Close x button clicked");
    modal.style.display = 'none';
  });

  nextStep1Btn.addEventListener('click', () => {
    console.log("Next step 1 button clicked");
    currentStep = 2;
      showStep(currentStep);
  });

  prevStep2Btn.addEventListener('click', () => {
    console.log("Previous step 2 button clicked");
    currentStep = 1;
      showStep(currentStep);
  });

  nextStep2Btn.addEventListener('click', () => {
    console.log("Next step 2 button clicked");
    currentStep = 3;
      showStep(currentStep);
  });

  window.addEventListener('click', (event) => {
      if (event.target === modal) {
        console.log("Modal background clicked");
        modal.style.display = 'none';
      }
  });
});