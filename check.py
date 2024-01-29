function getPreviousMonth() {
    let currentDate = new Date();
    console.log(typeof currentDate);

    currentDate.setMonth(currentDate.getMonth() - 1); // Subtract 1 month
    const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    const previousMonth = monthNames[currentDate.getMonth()] + '-' + currentDate.getFullYear();
    return previousMonth;
}

console.log(getPreviousMonth());
