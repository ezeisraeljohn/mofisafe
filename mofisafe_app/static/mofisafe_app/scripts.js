$(document).ready(function () {
  // Get the total income available

  $.ajax({
    url: "http://127.0.0.1:8000/api/v1/categories/",
    method: "GET",
    headers: {
      Authorization: "Basic " + btoa("ezeisraeljohn:testuser123"),
    },
    success: function (data) {
      let totalAmount = 0;
      data.forEach(function (category) {
        totalAmount += parseFloat(category.category_balance);
      });
      const formattedAmount = totalAmount.toFixed(2).toLocaleString();
      $(".balance").text(`$${formattedAmount}`);
    },
  });

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

  // This function gets the week of the month
  function getWeekOfMonth(date) {
    const firstDayOfMonth = moment(date).startOf("month");
    const weekOfYear = moment(date).week();
    const firstWeekOfYear = firstDayOfMonth.week();

    return weekOfYear - firstWeekOfYear + 1;
  }

  $.ajax({
    url: "http://127.0.0.1:8000/api/v1/income/",
    method: "GET",
    headers: {
      Authorization: "Basic " + btoa("ezeisraeljohn:testuser123"),
    },
    success: function (data) {
      const list = new Array(7).fill(0);
      const currentDate = moment().startOf("day"); // Get the current date and reset the time to midnight
      let total_weekly_income = 0;

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
      console.log(list);
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

  const getChartOptions = () => {
    return {
      series: [35.1, 23.5, 2.4, 5.4],
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
                label: "Unique visitors",
                fontFamily: "Inter, sans-serif",
                formatter: function (w) {
                  const sum = w.globals.seriesTotals.reduce((a, b) => {
                    return a + b;
                  }, 0);
                  return "$" + sum + "k";
                },
              },
              value: {
                show: true,
                fontFamily: "Inter, sans-serif",
                offsetY: -20,
                formatter: function (value) {
                  return value + "k";
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
      labels: ["Direct", "Sponsor", "Affiliate", "Email marketing"],
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
            return value + "k";
          },
        },
      },
      xaxis: {
        labels: {
          formatter: function (value) {
            return value + "k";
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

    // Get all the checkboxes by their class name
    const checkboxes = $('#devices input[type="checkbox"]');

    // Function to handle the checkbox change event
    function handleCheckboxChange(event) {
      const checkbox = event.target;
      if (checkbox.checked) {
        switch (checkbox.value) {
          case "desktop":
            chart.updateSeries([15.1, 22.5, 4.4, 8.4]);
            break;
          case "tablet":
            chart.updateSeries([25.1, 26.5, 1.4, 3.4]);
            break;
          case "mobile":
            chart.updateSeries([45.1, 27.5, 8.4, 2.4]);
            break;
          default:
            chart.updateSeries([55.1, 28.5, 1.4, 5.4]);
        }
      } else {
        chart.updateSeries([35.1, 23.5, 2.4, 5.4]);
      }
    }

    // Attach the event listener to each checkbox
    checkboxes.each(function () {
      $(this).on("change", handleCheckboxChange);
    });
  }

  const chartOptions = {
    yaxis: {
      show: false,
      labels: {
        formatter: function (value) {
          return "€" + value;
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
        name: "Developer Edition",
        data: [1500, 1418, 1456, 1526, 1356, 1256],
        color: "#1A56DB",
      },
      {
        name: "Designer Edition",
        data: [643, 413, 765, 412, 1423, 1731],
        color: "#7E3BF2",
      },
    ],
    xaxis: {
      categories: [
        "01 Feb",
        "02 Feb",
        "03 Feb",
        "04 Feb",
        "05 Feb",
        "06 Feb",
        "07 Feb",
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
});
