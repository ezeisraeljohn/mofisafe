$(document).ready(function () {
  const crsfToken = $("meta[name=crsf-token").attr("content");
  let total_weekly_income = 0;
  let total_weekly_expense = [];
  const list = new Array(7).fill(0);
  const list_expense = new Array(7).fill(0);

  // This function gets the week of the month
  function getWeekOfMonth(date) {
    const firstDayOfMonth = moment(date).startOf("month");
    const weekOfYear = moment(date).week();
    const firstWeekOfYear = firstDayOfMonth.week();

    return weekOfYear - firstWeekOfYear + 1;
  }
  // Gets Available Balance
  $.ajax({
    url: "http://127.0.0.1:8000/api/v1/categories/",
    method: "GET",
    headers: {
      Authorization: "Basic " + btoa("ezeisraeljohn:testuser123"),
    },
    success: function (data) {
      let totalAmount = 0;
      data.forEach(function (category) {
        if (category.type === "income") {
          totalAmount += parseFloat(category.category_balance);
        }
      });
      const formattedAmount = totalAmount.toFixed(2).toLocaleString();
      $(".balance").text(`$${formattedAmount}`);
    },
  });

  // Gets the total expense for a month
  $.ajax({
    url: "http://127.0.0.1:8000/api/v1/expenses/",
    method: "GET",
    headers: {
      Authorization: "Basic " + btoa("ezeisraeljohn:testuser123"),
    },
    success: function (data) {
      let totalAmount = 0;
      data.forEach(function (expense) {
        const the_date = moment(expense.date);
        if (the_date.month() === moment().month()) {
          totalAmount += parseFloat(expense.amount);
        }
      });
      const formattedAmount = totalAmount.toFixed(2).toLocaleString();
      $(".total-expense").text(`$${formattedAmount}`);
    },
  });

  // Get the total income for a week a create a chart for it
  $.ajax({
    url: "http://127.0.0.1:8000/api/v1/income/",
    method: "GET",
    headers: {
      Authorization: "Basic " + btoa("ezeisraeljohn:testuser123"),
    },
    success: function (data) {
      let totalAmount = 0;
      data.forEach(function (income) {
        const the_date = moment(income.date);
        if (the_date.month() === moment().month()) {
          totalAmount += parseFloat(income.amount);
        }
      });
      const formattedAmount = totalAmount.toFixed(2).toLocaleString();
      $(".monthly-saving").text(`$${formattedAmount}`);
    },
  });

  $.ajax({
    url: "http://127.0.0.1:8000/api/v1/income/",
    method: "GET",
    headers: {
      Authorization: "Basic " + btoa("ezeisraeljohn:testuser123"),
    },
    success: function (data) {
      const currentDate = moment().startOf("day"); // Get the current date and reset the time to midnight

      data.forEach(function (income) {
        const income_date = moment(income.date, "YYYY-MM-DD").startOf("day"); // Reset the time to midnight for the income date

        // Check if the income date is in the same week of the month as the current date
        if (getWeekOfMonth(income_date) === getWeekOfMonth(currentDate)) {
          const dayOfWeek = income_date.day();
          list[dayOfWeek] += parseFloat(income.amount);
          total_weekly_income += parseFloat(income.amount);
        }
        $(".income-week").text(`$${total_weekly_income}`);
      });

      // Create a chart for the weekly income
      const areaChartOptions = {
        chart: {
          height: "350",
          maxWidth: "100%",
          type: "area",
          fontFamily: "Inter, sans-serif",
          dropShadow: {
            enabled: false,
          },
          toolbar: {
            show: false,
          },
        },
        tooltip: {
          enabled: true,
          x: {
            show: false,
          },
        },
        fill: {
          type: "gradient",
          gradient: {
            opacityFrom: 0.55,
            opacityTo: 0,
            shade: "#1C64F2",
            gradientToColors: ["#1C64F2"],
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          width: 6,
        },
        grid: {
          show: false,
          strokeDashArray: 4,
          padding: {
            left: 2,
            right: 2,
            top: 0,
          },
        },
        series: [
          {
            name: "Income",
            data: list,
            color: "#1A56DB",
          },
        ],
        xaxis: {
          categories: [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
          ],
          labels: {
            show: false,
          },
          axisBorder: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
        },
        yaxis: {
          show: false,
        },
      };

      if ($("#area-chart").length && typeof ApexCharts !== "undefined") {
        const chart = new ApexCharts(
          document.getElementById("area-chart"),
          areaChartOptions
        );
        chart.render();
      }
    },
  });

  // This gets categories and create a chart for it
  $.ajax({
    url: "http://127.0.0.1:8000/api/v1/categories/",
    method: "GET",
    headers: {
      Authorization: "Basic " + btoa("ezeisraeljohn:testuser123"),
    },
    success: function (data) {
      const dict = {};
      data.forEach(function (cat) {
        if (cat.type === "income") {
          if (!dict[cat.name]) {
            dict[cat.name] = parseFloat(cat.category_balance);
          } else {
            dict[cat.name] += parseFloat(cat.category_balance);
          }
        }
      });
      console.log(dict);
      const series = [];
      const labels = [];
      for (const [label, serie] of Object.entries(dict)) {
        series.push(serie);
        labels.push(label);
      }
      const getChartOptions = () => {
        return {
          series: series,
          colors: ["#1C64F2", "#16BDCA", "#FDBA8C", "#E74694"],
          chart: {
            height: 350,
            width: "100%",
            type: "donut",
          },
          stroke: {
            colors: ["transparent"],
            lineCap: "",
          },
          plotOptions: {
            pie: {
              donut: {
                labels: {
                  show: true,
                  name: {
                    show: true,
                    fontFamily: "Inter, sans-serif",
                    offsetY: 20,
                  },
                  total: {
                    showAlways: true,
                    show: true,
                    label: "In Income",
                    fontFamily: "Inter, sans-serif",
                    formatter: function (w) {
                      const sum = w.globals.seriesTotals.reduce((a, b) => {
                        return a + b;
                      }, 0);
                      return "$" + sum;
                    },
                  },
                  value: {
                    show: true,
                    fontFamily: "Inter, sans-serif",
                    offsetY: -20,
                    formatter: function (value) {
                      return "$" + value;
                    },
                  },
                },
                size: "80%",
              },
            },
          },
          grid: {
            padding: {
              top: -2,
            },
          },
          labels: labels,
          dataLabels: {
            enabled: false,
          },
          legend: {
            position: "bottom",
            fontFamily: "Inter, sans-serif",
          },
          yaxis: {
            labels: {
              formatter: function (value) {
                return "$" + value;
              },
            },
          },
          xaxis: {
            labels: {
              formatter: function (value) {
                return "$" + value;
              },
            },
            axisTicks: {
              show: false,
            },
            axisBorder: {
              show: false,
            },
          },
        };
      };

      if ($("#donut-chart").length && typeof ApexCharts !== "undefined") {
        const chart = new ApexCharts(
          document.getElementById("donut-chart"),
          getChartOptions()
        );
        chart.render();
      }
    },
  });

  $.ajax({
    url: "http://127.0.0.1:8000/api/v1/expenses/",
    method: "GET",
    headers: {
      Authorization: "Basic " + btoa("ezeisraeljohn:testuser123"),
    },
    success: function (data) {
      const currentDate = moment().startOf("day"); // Get the current date and reset the time to midnight

      data.forEach(function (expense) {
        const expense_date = moment(expense.date, "YYYY-MM-DD").startOf("day"); // Reset the time to midnight for the income date

        // Check if the income date is in the same week of the month as the current date
        if (getWeekOfMonth(expense_date) === getWeekOfMonth(currentDate)) {
          const dayOfWeek = expense_date.day();
          list_expense[dayOfWeek] += parseFloat(expense.amount);
          total_weekly_expense += parseFloat(expense.amount);
        }
        // $(".income-week").text(`$${total_weekly_income}`);
      });
      const chartOptions = {
        yaxis: {
          show: false,
          labels: {
            formatter: function (value) {
              return "$" + value;
            },
          },
        },
        chart: {
          height: 350,
          maxWidth: "100%",
          type: "area",
          fontFamily: "Inter, sans-serif",
          dropShadow: {
            enabled: false,
          },
          toolbar: {
            show: false,
          },
        },
        tooltip: {
          enabled: true,
          x: {
            show: false,
          },
        },
        fill: {
          type: "gradient",
          gradient: {
            opacityFrom: 0.55,
            opacityTo: 0,
            shade: "#1C64F2",
            gradientToColors: ["#1C64F2"],
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          width: 6,
        },
        grid: {
          show: false,
          strokeDashArray: 4,
          padding: {
            left: 2,
            right: 2,
            top: -26,
          },
        },
        series: [
          {
            name: "Income",
            data: list,
            color: "#1A56DB",
          },
          {
            name: "Expenses",
            data: list_expense,
            color: "#7E3BF2",
          },
        ],
        xaxis: {
          categories: [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
          ],
          labels: {
            show: false,
          },
          axisBorder: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
        },
      };

      if ($("#main-chart").length && typeof ApexCharts !== "undefined") {
        const chart = new ApexCharts($("#main-chart")[0], chartOptions);
        chart.render();
      }
    },
  });
  // Fetch categories and populate the dropdown for adding income and expense
  $.ajax({
    url: "http://127.0.0.1:8000/api/v1/categories/",
    method: "GET",
    headers: {
      Authorization: "Basic " + btoa("ezeisraeljohn:testuser123"),
    },
    success: function (data) {
      data.forEach(function (category) {
        if (category.type === "income") {
          $("#add-expense-category, #add-income-category").append(
            `<option value="${category.id}">${category.name}</option>`
          );
        }
      });
    },
  });

  // Handle Expense Submittion
  $("#add-expense-form").on("submit", function (event) {
    event.preventDefault();
    const data = {
      amount: $("#add-expense-amount").val(),
      date: $("#add-expense-date").val(),
      description: $("#add-expense-description").val(),
      category: $("#add-expense-category").val(),
    };

    $.ajax({
      url: "http://127.0.0.1:8000/api/v1/expenses/",
      method: "POST",
      headers: {
        Authorization: "Basic " + btoa("ezeisraeljohn:testuser123"),
        "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
        "Content-Type": "application/json",
      },
      data: JSON.stringify(data),
      success: function (response) {
        $(".goes").text("Expense added successfully!");
        location.reload();
      },
      error: function (xhr, errmsg, err) {
        $(".goes").text("Failed to add expense.");
        let response = JSON.parse(xhr.responseText);
        if (response.detail) {
          alert("Error: " + response.detail);
        } else {
          alert("An error occurred: " + xhr.responseText);
        }
      },
    });
  });

  // Handle Income Submittion
  $("#add-income-form").on("submit", function (event) {
    event.preventDefault();
    const data = {
      amount: $("#add-income-amount").val(),
      date: $("#add-income-date").val(),
      source: $("#add-income-source").val(),
      category: $("#add-income-category").val(),
    };

    $.ajax({
      url: "http://127.0.0.1:8000/api/v1/income/",
      method: "POST",
      headers: {
        Authorization: "Basic " + btoa("ezeisraeljohn:testuser123"),
        "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
        "Content-Type": "application/json",
      },
      data: JSON.stringify(data),
      success: function (response) {
        $(".goes").text(data);
        location.reload();
      },
      error: function (xhr, errmsg, err) {
        let response = JSON.parse(xhr.responseText);
        if (response.detail) {
          alert("Error: " + response.detail);
        } else {
          alert("An error occurred: " + xhr.responseText);
        }
      },
    });
  });
});
