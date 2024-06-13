const monthMap = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
};

data.sort((a, b) => {
    const [monthA, yearA] = a.month.split('-');
    const [monthB, yearB] = b.month.split('-');
    return yearA - yearB || monthMap[monthA] - monthMap[monthB];
});

const series = Object.values(data.reduce((acc, { type_name, type_count }) => {
    if (!acc[type_name]) {
        acc[type_name] = { name: type_name, data: [] };
    }
    acc[type_name].data.push(type_count);
    return acc;
}, {}));
