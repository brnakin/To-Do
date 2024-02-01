document.addEventListener('DOMContentLoaded', function () {
  const actionItems = document.querySelectorAll('.action-item')

  actionItems.forEach((item, index) => {
    item.addEventListener('click', function () {
      this.classList.toggle('checked')
    })
  })
})