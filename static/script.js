document.addEventListener('DOMContentLoaded', function () {
  const actionItems = document.querySelectorAll('.action-item')

  actionItems.forEach((item, index) => {
    item.addEventListener('click', function () {
      this.classList.toggle('checked')
    })
  })
})

document.getElementById("submitBtn").addEventListener("click", function () {
  // Add the "loading" class to the button to trigger the loading spinner
  this.classList.add("loading");

  // Simulate an asynchronous operation (e.g., AJAX request)
  setTimeout(function () {
    // Remove the "loading" class after the operation is complete
    document.getElementById("submitBtn").classList.remove("loading");
  }, 3000); // Simulated delay of 3 seconds (adjust as needed)
});
