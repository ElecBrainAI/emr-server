<script setup>
import { onMounted } from 'vue';
import { initFlowbite } from 'flowbite';
import { FwbButton } from 'flowbite-vue';
import 'https://unpkg.com/phosphor-icons';

onMounted(() => {
    initFlowbite();
})

// ApexCharts options and config
window.addEventListener("load", function() {
  let options = {
    // set the labels option to true to show the labels on the X and Y axis
    xaxis: {
      show: true,
      categories: ['01 Feb', '02 Feb', '03 Feb', '04 Feb', '05 Feb', '06 Feb', '07 Feb'],
      labels: {
        show: true,
        style: {
          fontFamily: "Inter, sans-serif",
          cssClass: 'text-xs font-normal fill-gray-500 dark:fill-gray-400'
        }
      },
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
    },
    yaxis: {
      show: true,
      labels: {
        show: true,
        style: {
          fontFamily: "Inter, sans-serif",
          cssClass: 'text-xs font-normal fill-gray-500 dark:fill-gray-400'
        },
        formatter: function (value) {
          return '$' + value;
        }
      }
    },
    series: [
      {
        name: "Developer Edition",
        data: [150, 141, 145, 152, 135, 125],
        color: "#1A56DB",
      },
      {
        name: "Designer Edition",
        data: [43, 13, 65, 12, 42, 73],
        color: "#7E3BF2",
      },
    ],
    chart: {
      sparkline: {
        enabled: false
      },
      height: "100%",
      width: "100%",
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
    legend: {
      show: false
    },
    grid: {
      show: false,
    },
  }

  if (document.getElementById("labels-chart") && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(document.getElementById("labels-chart"), options);
    chart.render();
  }
});

</script>

<template>
  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lilita+One&family=Righteous&family=Song+Myung&family=Varela+Round&display=swap" rel="stylesheet">
    <title></title>
  </head>
  <body>
    <!-- Patient Info modal -->
    <div id="p-info-modal" tabindex="0" aria-hidden="true" class="modal hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-1000 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-[640px] max-h-full">
            <!-- Modal content -->
            <div class="modal relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-2 md:p-2 border-b rounded-t dark:border-gray-600 ml-2">
                    <h3 class="flex flex-row items-center text-xs font-semibold text-gray-600 dark:text-white">
                        <svg class="w-3 h-3 mr-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 18">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm-2 3h4a4 4 0 0 1 4 4v2H1v-2a4 4 0 0 1 4-4Z"/>
                        </svg>
                        환자정보상세
                    </h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="p-info-modal">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <form class="p-4 md:p-5">

                    <div class="grid gap-6 mb-6 md:grid-cols-1">
                        <div>
                            <label for="name" class="block mb-2 text-xs font-medium text-gray-600 dark:text-white">이름*</label>
                            <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="김메디" required>
                        </div>
                      </div>
                    <div class="grid gap-6 mb-6 md:grid-cols-2">
                        <div>
                          <label for="resident" class="block mb-2 text-xs font-medium text-gray-600 dark:text-white">주민등록번호(외국인등록번호)*</label>
                          <div class="flex flex-row">
                            <input type="text" id="resident" class="mr-1 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="031006" required>
                            <input type="text" id="resident" class="ml-1 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="4999999" required>
                          </div>
                        </div>
                        <div class="flex items-center">
                          <div class="flex items-center">
                              <input checked id="checked-checkbox" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                              <label for="checked-checkbox" class="ms-2 text-xs font-medium text-gray-900 dark:text-gray-300">주민등록번호가 없습니다.</label>
                          </div>
                        </div>
                        <div>
                            <label for="phone1" class="block mb-2 text-xs font-medium text-gray-600 dark:text-white">대표 연락처</label>
                            <input type="tel" id="phone" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="010-1111-1111" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" required>
                        </div>
                        <div>
                            <label for="phone2" class="block mb-2 text-xs font-medium text-gray-600 dark:text-white">비상 연락처</label>
                            <input type="url" id="website" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="flowbite.com" required>
                        </div>
                    </div>
                    <div class="grid gap-6 md:grid-cols-2">
                        <div>
                            <label for="address" class="block mb-2 text-xs font-medium text-gray-600 dark:text-white">주소</label>
                            <div class="relative mb-2">
                                <div class="absolute inset-y-0 start-0 top-0 flex items-center ps-3.5 pointer-events-none">
                                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
                                        <path d="M8 0a7.992 7.992 0 0 0-6.583 12.535 1 1 0 0 0 .12.183l.12.146c.112.145.227.285.326.4l5.245 6.374a1 1 0 0 0 1.545-.003l5.092-6.205c.206-.222.4-.455.578-.7l.127-.155a.934.934 0 0 0 .122-.192A8.001 8.001 0 0 0 8 0Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z"/>
                                    </svg>
                                </div>
                                <input type="text" id="zip-input" aria-describedby="helper-text-explanation" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="12345 or 12345-6789" pattern="^\d{5}(-\d{4})?$" required>
                            </div>
                        </div>
                    </div>
                    <div class="grid mb-6 md:grid-cols-1">
                            <div class="mb-2">
                                <input type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="도로명 주소" required>
                            </div>
                            <div class="mb-2">
                                <input type="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="상세주소" required>
                            </div>
                    </div>
                    <div class="flex justify-between">
                      <button type="submit" class="text-gray-600 bg-white border border-gray-200 hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800">취소</button>
                      <button type="submit" class="text-white bg-sky-blue hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">수정</button>
                    </div>
                </form>

            </div>
        </div>
    </div>

    <!-- Family list modal -->
    <div id="family-list-modal" tabindex="0" aria-hidden="true" class="modal hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-1000 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-[440px] max-h-full">
            <!-- Modal content -->
            <div class="modal relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-2 md:p-2 border-b rounded-t dark:border-gray-600 ml-2">
                    <h3 class="flex flex-row items-center text-xs font-semibold text-gray-600 dark:text-white">
                        가족관계
                    </h3>


                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="family-list-modal">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <form class="p-4 md:p-5">

                    <div class="grid gap-6 mb-6 md:grid-cols-1">
                      <p class="flex flex-row text-xs font-normal items-center">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                          <path d="M16 0H4a2 2 0 0 0-2 2v1H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v1a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4.5a3 3 0 1 1 0 6 3 3 0 0 1 0-6ZM13.929 17H7.071a.5.5 0 0 1-.5-.5 3.935 3.935 0 1 1 7.858 0 .5.5 0 0 1-.5.5Z"/>
                        </svg>
                        <a class="ml-1 font-semibold">이아들</a>
                        <span class="ml-1">남 11세</span>
<!--                          <span class="ml-4">-->
<!--                            <button type="button" class="flex flex-row items-center">-->
<!--                              <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">-->
<!--                                <path d="M18 7.5h-.423l-.452-1.09.3-.3a1.5 1.5 0 0 0 0-2.121L16.01 2.575a1.5 1.5 0 0 0-2.121 0l-.3.3-1.089-.452V2A1.5 1.5 0 0 0 11 .5H9A1.5 1.5 0 0 0 7.5 2v.423l-1.09.452-.3-.3a1.5 1.5 0 0 0-2.121 0L2.576 3.99a1.5 1.5 0 0 0 0 2.121l.3.3L2.423 7.5H2A1.5 1.5 0 0 0 .5 9v2A1.5 1.5 0 0 0 2 12.5h.423l.452 1.09-.3.3a1.5 1.5 0 0 0 0 2.121l1.415 1.413a1.5 1.5 0 0 0 2.121 0l.3-.3 1.09.452V18A1.5 1.5 0 0 0 9 19.5h2a1.5 1.5 0 0 0 1.5-1.5v-.423l1.09-.452.3.3a1.5 1.5 0 0 0 2.121 0l1.415-1.414a1.5 1.5 0 0 0 0-2.121l-.3-.3.452-1.09H18a1.5 1.5 0 0 0 1.5-1.5V9A1.5 1.5 0 0 0 18 7.5Zm-8 6a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Z"/>-->
<!--                              </svg>-->
<!--                              <span class="ml-1">정보수정</span>-->
<!--                            </button>-->
<!--                          </span>-->
                      </p>
                    </div>


                    <div class="flex justify-between">
                      <button type="button" data-modal-target="add-family-list-modal" data-modal-toggle="add-family-list-modal" class="text-gray-600 bg-white border border-gray-200 hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800">가족추가</button>
                      <button type="button" data-modal-toggle="family-list-modal" class="text-white bg-sky-blue hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">닫기</button>
                    </div>
                </form>

            </div>
        </div>
    </div>


    <!-- Add Family list modal -->
    <div id="add-family-list-modal" tabindex="0" aria-hidden="true" class="modal hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-1000 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-[440px] max-h-full">
            <!-- Modal content -->
            <div class="modal relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-2 md:p-2 border-b rounded-t dark:border-gray-600 ml-2">
                    <h3 class="flex flex-row items-center text-xs font-semibold text-gray-600 dark:text-white">
                        가족추가
                    </h3>


                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="add-family-list-modal">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <form class="p-4 md:p-5">

                    <div class="grid gap-6 mb-6 md:grid-cols-1">

                          <label for="default-search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
                          <div class="flex flex-row relative">
                              <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                                  <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                                  </svg>
                              </div>
                              <input type="search" id="default-search" class="w-[150%] block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="환자검색" required>
                              <select id="countries" class="ml-4 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                <option selected>관계 선택</option>
                                <option value="FA">부</option>
                                <option value="MA">모</option>
                                <option value="SP">배우자</option>
                                <option value="SIB">형제</option>
                                <option value="SIS">자매</option>
                                <option value="CHILD">자녀</option>
                                <option value="GF">조부</option>
                                <option value="GM">조모</option>
                              </select>
                          </div>

                    </div>


                    <div class="flex justify-between">
                      <button type="button" data-modal-toggle="add-family-list-modal" class="text-gray-600 bg-white border border-gray-200 hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800">취소</button>
                      <button type="button" data-modal-toggle="add-family-list-modal"  class="text-white bg-sky-blue hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">저장</button>
                    </div>
                </form>

            </div>
        </div>
    </div>

    <!-- Inbody modal -->
    <div id="inbody-modal" tabindex="0" aria-hidden="true" class="modal hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-1000 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-[640px] max-h-full">
            <!-- Modal content -->
            <div class="modal relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-2 md:p-2 border-b rounded-t dark:border-gray-600 ml-2">
                    <h3 class="flex flex-row items-center text-xs font-semibold text-gray-600 dark:text-white">
                        <svg class="w-3 h-3 mr-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 18">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm-2 3h4a4 4 0 0 1 4 4v2H1v-2a4 4 0 0 1 4-4Z"/>
                        </svg>
                        Inbody 기록
                    </h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="inbody-modal">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <form class="p-4 md:p-5">
                    <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white pb-2 border-b-2">2022-02-16 10:16</label>
                    <div class="grid gap-6 mb-10 md:grid-cols-6">
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">체중</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="kg" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">체지방률</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="%" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">근육량</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="%" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">기초대사량</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="kal" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">비만도지수</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="kg/m^2" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">수분함량</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="%" required>
                      </div>
                    </div>

                    <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white pb-2 border-b-2">과거내역</label>
                    <div class="grid gap-6 mb-6 md:grid-cols-6">
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">체중</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">0kg</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">체지방률</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">0%</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">근육량</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">0%</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">기초대사량</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">0kal</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">비만도지수</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">0kg/m^2</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">수분함량</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">0%</span>
                      </div>
                    </div>

                    <div class="flex justify-between">
                      <button type="submit" class="text-gray-600 bg-white border border-gray-200 hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800">취소</button>
                      <button type="submit" class="text-white bg-sky-blue hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">확인</button>
                    </div>
                </form>

            </div>
        </div>
    </div>

    <!-- X-ray modal -->
    <div id="x-ray-modal" tabindex="0" aria-hidden="true" class="modal hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-1000 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-[640px] max-h-full">
            <!-- Modal content -->
            <div class="modal relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-2 md:p-2 border-b rounded-t dark:border-gray-600 ml-2">
                    <h3 class="flex flex-row items-center text-xs font-semibold text-gray-600 dark:text-white">
                        <svg class="w-3 h-3 mr-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 18">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm-2 3h4a4 4 0 0 1 4 4v2H1v-2a4 4 0 0 1 4-4Z"/>
                        </svg>
                        X-ray 기록
                    </h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="x-ray-modal">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <form class="p-4 md:p-5">
                    <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white pb-2 border-b-2">2022-02-16 10:16</label>
                    <div class="grid gap-6 mb-10 md:grid-cols-4">
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">촬영장비</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="kg" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">촬영부위</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="%" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">촬영담당</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="kg/m^2" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">사진</label>
                          <div class="flex items-center justify-center w-full">
                              <label for="dropzone-file" class="flex flex-col p-2 items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                                  <div class="flex flex-col items-center justify-center pt-5 pb-6">
                                      <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                                      </svg>
                                      <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                                      <p class="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
                                  </div>
                                  <input id="dropzone-file" type="file" class="hidden" />
                              </label>
                          </div>

                      </div>
                    </div>

                    <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white pb-2 border-b-2">과거내역</label>
                    <div class="grid gap-6 mb-6 md:grid-cols-4">
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">촬영장비</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">mri</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">촬영부위</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">발목</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">촬영담당</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">홍길동</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">사진</label>
                          <span class="mb-2 text-xs font-bold text-gray-400"><a href="#">사진</a></span>
                      </div>
                    </div>

                    <div class="flex justify-between">
                      <button type="submit" class="text-gray-600 bg-white border border-gray-200 hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800">취소</button>
                      <button type="submit" class="text-white bg-sky-blue hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">확인</button>
                    </div>
                </form>

            </div>
        </div>
    </div>

    <!-- treatment modal -->
    <div id="treatment-modal" tabindex="0" aria-hidden="true" class="modal hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-1000 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-[640px] max-h-full">
            <!-- Modal content -->
            <div class="modal relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-2 md:p-2 border-b rounded-t dark:border-gray-600 ml-2">
                    <h3 class="flex flex-row items-center text-xs font-semibold text-gray-600 dark:text-white">
                        <svg class="w-3 h-3 mr-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 18">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm-2 3h4a4 4 0 0 1 4 4v2H1v-2a4 4 0 0 1 4-4Z"/>
                        </svg>
                        진료 기록
                    </h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="treatment-modal">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <form class="p-4 md:p-5">
                    <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white pb-2 border-b-2">2022-02-16 10:16</label>
                    <div class="grid gap-6 mb-10 md:grid-cols-4">
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">윗몸일으키기</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="(횟수/분)" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">버피</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="(횟수/분)" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">왕복 오래달리기</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="횟수" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">인터벌 트레이닝</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="분" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">제자리 멀리뛰기</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="cm" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">사이드 스템</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="(횟수/분)" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">앉아윗몸앞으로굽히기</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="cm" required>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">요가</label>
                          <input type="text" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="분" required>
                      </div>
                    </div>

                    <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white pb-2 border-b-2">과거내역</label>
                    <div class="grid gap-6 mb-6 md:grid-cols-4">
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">윗몸일으키기</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">(0개/0분)</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">버피</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">(0개/0분)</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">왕복 오래달리기</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">0번</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">인터벌 트래이닝</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">0분</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">제자리 멀리뛰기</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">0cm</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">사이드 스템</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">(0개/0분)</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">앉아윗몸앞으로굽히기</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">0cm</span>
                      </div>
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">요가</label>
                          <span class="mb-2 text-xs font-bold text-gray-400">0분</span>
                      </div>
                    </div>

                    <div class="flex justify-between">
                      <button type="submit" class="text-gray-600 bg-white border border-gray-200 hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800">취소</button>
                      <button type="submit" class="text-white bg-sky-blue hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">확인</button>
                    </div>
                </form>

            </div>
        </div>
    </div>

    <!-- prescription modal -->
    <div id="prescription-modal" tabindex="0" aria-hidden="true" class="modal hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-1000 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-[640px] max-h-full">
            <!-- Modal content -->
            <div class="modal relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-2 md:p-2 border-b rounded-t dark:border-gray-600 ml-2">
                    <h3 class="flex flex-row items-center text-xs font-semibold text-gray-600 dark:text-white">
                        <svg class="w-3 h-3 mr-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 18">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm-2 3h4a4 4 0 0 1 4 4v2H1v-2a4 4 0 0 1 4-4Z"/>
                        </svg>
                        진단 및 처방
                    </h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-toggle="prescription-modal">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <form class="p-4 md:p-5">
                    <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white pb-2 border-b-2">2022-02-16 10:16</label>
                    <div class="grid gap-6 mb-10 ">
                      <div>
                        <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">진단</label>
                        <textarea type="text" id="name" class="content-grid-textbox" placeholder="진단을 적어주세요." required></textarea>
                      </div>

                    </div>

                    <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white pb-2 border-b-2">2022-02-16 10:16</label>
                    <div class="grid gap-6 mb-6 ">
                      <div>
                          <label for="name" class="block mb-2 text-xs font-bold text-gray-600 dark:text-white">처방</label>
                          <textarea type="text" id="name" class="content-grid-textbox" placeholder="처방을 적어주세요." required></textarea>
                      </div>
                    </div>

                    <div class="flex justify-between">
                      <button type="submit" class="text-gray-600 bg-white border border-gray-200 hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800">취소</button>
                      <button type="submit" class="text-white bg-sky-blue hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">확인</button>
                    </div>
                </form>

            </div>
        </div>
    </div>


    <div class="static h-screen flex overflow-hidden">
      <!-- SIDEBAR -->
      <div class="main-bar w-48 py-4 px-8 bg-gray-100 border-r overflow-auto">
        <button data-drawer-target="logo-sidebar" data-drawer-toggle="logo-sidebar" aria-controls="logo-sidebar" type="button" class="inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
          <span class="sr-only">Open sidebar</span>
          <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path clip-rule="evenodd" fill-rule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
          </svg>
        </button>
        <aside id="logo-sidebar" class="fixed top-0 left-0 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0" aria-label="Sidebar">
          <div class="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
            <a href="/" class="flex items-center ps-2.5 mb-5">
              <span class="title self-center text-xl font-semibold whitespace-nowrap dark:text-white">EMR</span>
            </a>
            <ul class="space-y-2 font-medium sidebar">
              <li>
                <a href="/" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                  <svg class="w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z"/>
                  </svg>
                  <span class="ms-3 sidebar-home">홈</span>
                </a>
              </li>
              <li>
                <a href="#" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                  <svg class="w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 21">
                    <path d="M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z"/>
                    <path d="M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z"/>
                  </svg>
                  <span class="flex-1 ms-3 whitespace-nowrap">차트</span>
<!--                  <span class="inline-flex items-center justify-center px-2 ms-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">Pro</span>-->
                </a>
              </li>
<!--              <li>-->
<!--                <a href="#" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">-->
<!--                  <svg class="w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">-->
<!--                    <path d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 8v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0Zm12 7h-1v1a1 1 0 0 1-2 0v-1H8a1 1 0 0 1 0-2h1v-1a1 1 0 1 1 2 0v1h1a1 1 0 0 1 0 2Z"/>-->
<!--                  </svg>-->

<!--                  <span class="flex-1 ms-3 whitespace-nowrap">예약</span>-->
<!--                  <span class="inline-flex items-center justify-center w-3 h-3 p-3 ms-3 text-sm font-medium text-blue-800 bg-blue-100 rounded-full dark:bg-blue-900 dark:text-blue-300">3</span>-->
<!--                </a>-->
<!--              </li>-->
              <li>
                <a href="/reception" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                  <svg class="w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                    <path d="M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2ZM7 2h4v3H7V2Zm5.7 8.289-3.975 3.857a1 1 0 0 1-1.393 0L5.3 12.182a1.002 1.002 0 1 1 1.4-1.436l1.328 1.289 3.28-3.181a1 1 0 1 1 1.392 1.435Z"/>
                  </svg>
                  <span class="flex-1 ms-3 whitespace-nowrap">접수</span>
                </a>
              </li>
<!--              <li>-->
<!--                <a href="#" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">-->
<!--                  <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">-->
<!--                    <path d="M5 5V.13a2.96 2.96 0 0 0-1.293.749L.879 3.707A2.96 2.96 0 0 0 .13 5H5Z"/>-->
<!--                    <path d="M6.737 11.061a2.961 2.961 0 0 1 .81-1.515l6.117-6.116A4.839 4.839 0 0 1 16 2.141V2a1.97 1.97 0 0 0-1.933-2H7v5a2 2 0 0 1-2 2H0v11a1.969 1.969 0 0 0 1.933 2h12.134A1.97 1.97 0 0 0 16 18v-3.093l-1.546 1.546c-.413.413-.94.695-1.513.81l-3.4.679a2.947 2.947 0 0 1-1.85-.227 2.96 2.96 0 0 1-1.635-3.257l.681-3.397Z"/>-->
<!--                    <path d="M8.961 16a.93.93 0 0 0 .189-.019l3.4-.679a.961.961 0 0 0 .49-.263l6.118-6.117a2.884 2.884 0 0 0-4.079-4.078l-6.117 6.117a.96.96 0 0 0-.263.491l-.679 3.4A.961.961 0 0 0 8.961 16Zm7.477-9.8a.958.958 0 0 1 .68-.281.961.961 0 0 1 .682 1.644l-.315.315-1.36-1.36.313-.318Zm-5.911 5.911 4.236-4.236 1.359 1.359-4.236 4.237-1.7.339.341-1.699Z"/>-->
<!--                  </svg>-->
<!--                  <span class="flex-1 ms-3 whitespace-nowrap">진료</span>-->
<!--                </a>-->
<!--              </li>-->
              <li>
                <a href="/receive" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                  <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M18.017 15.002h-1.5v-1.5a1 1 0 0 0-2 0v1.5h-1.5a1 1 0 0 0 0 2h1.5v1.5a1 1 0 1 0 2 0v-1.5h1.5a1 1 0 1 0 0-2Z"/>
                    <path d="m17.74 4.758-7.476 8.409a1 1 0 0 1-.718.335h-.029a1 1 0 0 1-.707-.293l-4-4a1 1 0 0 1 1.414-1.413l3.25 3.25L16.53 3.11a9.5 9.5 0 1 0-3.885 15.355 2.495 2.495 0 0 1 .373-4.963 2.5 2.5 0 0 1 5 0c.035 0 .068.01.1.01a9.43 9.43 0 0 0-.38-8.754h.002Z"/>
                  </svg>
                  <span class="flex-1 ms-3 whitespace-nowrap">수납</span>
                </a>
              </li>
              <li class="sidebar-login">
                <router-link to="/login">
                  <a href="/login" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                    <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 16">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3"/>
                    </svg>
                    <span class="flex-1 ms-3 whitespace-nowrap">로그인</span>
                  </a>
                </router-link>
                <router-view/>
              </li>
            </ul>
          </div>
        </aside>

      </div>
      <div class="sub-chart-bar relative flex flex-col flex-1 min-w-0 overflow-auto">
        <header class="px-2 w-full bg-white border border-gray-200 rounded-lg dark:bg-gray-800 dark:border-gray-700">
          <nav class="flex h-full w-14 justify-center items-center" aria-label="Breadcrumb">
            <ol class="fixed inline-flex items-center">
                <div class="flex items-center align-item-center">
                  <a href="#" class="text-lg font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white">차트</a>
                </div>
            </ol>
          </nav>
          <div class="search-bar">
            <form class="flex items-center ml-2">
              <label for="simple-search" class="sr-only">Search</label>
              <div class="relative w-full mt-2 mb-2">
                <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                  <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 18">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm-2 3h4a4 4 0 0 1 4 4v2H1v-2a4 4 0 0 1 4-4Z"/>
                  </svg>
                </div>
                <input type="text" id="simple-search" class="search-input bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-0.55 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="환자검색(이름/차트번호/생년월일/휴대폰번호)" required>
              </div>
              <button type="submit" class="p-2.5 ms-2 text-sm bg-[#5A9FFE] font-medium text-white rounded-lg border border-white hover:bg-blue-800 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                </svg>
                <span class="sr-only">Search</span>
              </button>
              <div class="ml-2">

              </div>
              <button type="button" class="p-2.5 ms-2 text-sm font-medium text-white rounded-lg border border-[#5A9FFE] bg-white">
                <svg class="w-4 h-4 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="#5A9FFE" viewBox="0 0 20 18">
                  <path d="M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Zm11-3h-2V5a1 1 0 0 0-2 0v2h-2a1 1 0 1 0 0 2h2v2a1 1 0 0 0 2 0V9h2a1 1 0 1 0 0-2Z"/>
                </svg>
              </button>



            </form>
          </div>
        </header>
        <div class="inline-flex flex-row overflow-hidden">
          <div class="sticky h-screen w-80 bg-white border border-gray-200 rounded-lg dark:bg-gray-800 dark:border-gray-700 z-5">
            <div class="pb-2">
              <div class="sub-menu-p-list">
                <div class="flex px-4 pt-4 justify-between items-center">
                    <h5 class="ml-1 text-sm font-medium text-gray-800 dark:text-white">환자리스트</h5>
                    <button id="dropdownButton" data-dropdown-toggle="dropdown" class="inline-block text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:ring-4 focus:outline-none focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-1.5" type="button">
                        <span class="sr-only">Open dropdown</span>
                        <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 3">
                            <path d="M2 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm6.041 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM14 0a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Z"/>
                        </svg>
                    </button>
                    <!-- Dropdown menu -->
<!--                    <div id="dropdown" class="z-10 hidden text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">-->
<!--                        <ul class="py-2" aria-labelledby="dropdownButton">-->
<!--                        <li>-->
<!--                            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Edit</a>-->
<!--                        </li>-->
<!--                        <li>-->
<!--                            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Export Data</a>-->
<!--                        </li>-->
<!--                        <li>-->
<!--                            <a href="#" class="block px-4 py-2 text-sm text-red-600 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Delete</a>-->
<!--                        </li>-->
<!--                        </ul>-->
<!--                    </div>-->

                </div>
                <div class="flex px-4 pt-4 justify-between items-center grow-0">
                  <div class="text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:text-gray-400 dark:border-gray-700">
                      <ul class="flex flex-wrap -mb-px">
                          <li class="me-2">
                              <a href="#" class="inline-block p-1 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300">대기 6</a>
                          </li>
                          <li class="me-2">
                              <a href="#" class="inline-block p-1 text-sky-blue text-blue-600 border-sky border-b-2 border-blue-600 rounded-t-lg active dark:text-blue-500 dark:border-blue-500" aria-current="page">예약 0</a>
                          </li>
                          <li class="me-2">
                              <a href="#" class="inline-block p-1 border-b-2 border-transparent rounded-t-lg hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300">방문 2</a>
                          </li>
                      </ul>
                  </div>
                </div>
                <div class="flex px-4 pt-2 justify-end items-center">
                  <span class="text-gray-500 mr-1.5 text-xs font-semibold">
                    진료실01외 4
                  </span>
                  <svg class="w-2 h-2 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 8">
                    <path stroke="gray" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="m1 1 5.326 5.7a.909.909 0 0 0 1.348 0L13 1"/>
                  </svg>
                </div>
              </div>
            </div>
            <div class="patient-list-cards flex px-4 pt-2 items-center">


              <div id="accordion-open" data-accordion="open" class="w-full">

                <div id="t-room-1" class="mb-2">
                  <h2 id="accordion-open-heading-1">
                    <button type="button" class="flex items-center justify-between w-full p-3 font-medium rtl:text-right text-gray-500 border border-gray-200 rounded-t-xl hover:bg-gray-100 dark:hover:bg-gray-800 gap-3" data-accordion-target="#accordion-open-body-1" aria-expanded="true" aria-controls="accordion-open-body-1">
                      <span class="flex items-center text-sm"><svg class="w-5 h-5 me-2 shrink-0" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd"></path></svg>진료실01</span>
                      <span class="patient-num-each text-sm">
                        <span class="mr-2 mb-0.2">2</span>
                        <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5"/>
                        </svg>
                      </span>
                    </button>
                  </h2>
                  <div id="accordion-open-body-1" class="hidden" aria-labelledby="accordion-open-heading-1">
                    <div class="border border-gray-200 dark:border-gray-700 dark:bg-gray-900">
                      <ul role="list" class="max-w-sm divide-y divide-gray-200 dark:divide-gray-700 border rounded-b-xl">
                          <li class="py-2 sm:py-2">
                              <div class="flex items-center space-x-3 rtl:space-x-reverse">
                                  <div class="flex-shrink-0">
                                  </div>
                                  <div class="flex-1 min-w-0">
                                      <p class="text-sm font-normal text-gray-900 truncate dark:text-white ml-1">
                                          송혜교
                                      </p>
                                      <p class="text-sm text-gray-500 truncate dark:text-gray-400 ml-1">
                                          여 31세
                                      </p>
                                  </div>
                                  <span class="inline-flex items-center text-xs font-medium px-2.5 py-0.5 rounded-full">
                                    <span class="text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-blue-400 border border-blue-400">
                                      진행중
                                    </span>
                                  </span>
                              </div>
                          </li>
                          <li class="py-2 sm:py-2">
                              <div class="flex items-center space-x-3 rtl:space-x-reverse">
                                  <div class="flex-shrink-0">
                                  </div>
                                  <div class="flex-1 min-w-0">
                                      <p class="text-sm font-normal text-gray-900 truncate dark:text-white ml-1">
                                          김메디
                                      </p>
                                      <p class="text-sm text-gray-500 truncate dark:text-gray-400 ml-1">
                                          남 23세
                                      </p>
                                  </div>
                                  <span class="inline-flex items-center text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-red-900 dark:text-red-300">
                                      <span class="text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-green-400 border border-green-400">
                                        우선대기
                                      </span>
                                  </span>
                              </div>
                          </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div id="t-room-2" class="mb-2">
                  <h2 id="accordion-open-heading-2">
                    <button type="button" class="flex items-center justify-between w-full p-3 font-medium rtl:text-right text-gray-500 border border-gray-200 rounded-t-xl hover:bg-gray-100 dark:hover:bg-gray-800 gap-3" data-accordion-target="#accordion-open-body-2" aria-expanded="true" aria-controls="accordion-open-body-2">
                      <span class="flex items-center text-sm"><svg class="w-5 h-5 me-2 shrink-0" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd"></path></svg>진료실02</span>
                      <span class="patient-num-each text-sm">
                        <span class="mr-2 mb-0.2">2</span>
                        <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5"/>
                        </svg>
                      </span>
                    </button>
                  </h2>
                  <div id="accordion-open-body-2" class="hidden" aria-labelledby="accordion-open-heading-2">
                    <div class="border border-gray-200 dark:border-gray-700 dark:bg-gray-900">
                      <ul role="list" class="max-w-sm divide-y divide-gray-200 dark:divide-gray-700 border rounded-b-xl">
                          <li class="py-2 sm:py-2">
                              <div class="flex items-center space-x-3 rtl:space-x-reverse">
                                  <div class="flex-shrink-0">
                                  </div>
                                  <div class="flex-1 min-w-0">
                                      <p class="text-sm font-normal text-gray-900 truncate dark:text-white ml-1">
                                          송혜교
                                      </p>
                                      <p class="text-sm text-gray-500 truncate dark:text-gray-400 ml-1">
                                          여 31세
                                      </p>
                                  </div>
                                  <span class="inline-flex items-center text-xs font-medium px-2.5 py-0.5 rounded-full">
                                    <span class="text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-blue-400 border border-blue-400">
                                      진행중
                                    </span>
                                  </span>
                              </div>
                          </li>
                          <li class="py-2 sm:py-2">
                              <div class="flex items-center space-x-3 rtl:space-x-reverse">
                                  <div class="flex-shrink-0">
                                  </div>
                                  <div class="flex-1 min-w-0">
                                      <p class="text-sm font-normal text-gray-900 truncate dark:text-white ml-1">
                                          김메디
                                      </p>
                                      <p class="text-sm text-gray-500 truncate dark:text-gray-400 ml-1">
                                          남 23세
                                      </p>
                                  </div>
                                  <span class="inline-flex items-center text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-red-900 dark:text-red-300">
                                      <span class="text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-green-400 border border-green-400">
                                        우선대기
                                      </span>
                                  </span>
                              </div>
                          </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div id="t-room-3" class="mb-2">
                  <h2 id="accordion-open-heading-3">
                    <button type="button" class="flex items-center justify-between w-full p-3 font-medium rtl:text-right text-gray-500 border border-gray-200 rounded-t-xl hover:bg-gray-100 dark:hover:bg-gray-800 gap-3" data-accordion-target="#accordion-open-body-3" aria-expanded="true" aria-controls="accordion-open-body-3">
                      <span class="flex items-center text-sm"><svg class="w-5 h-5 me-2 shrink-0" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd"></path></svg>진료실02</span>
                      <span class="patient-num-each text-sm">
                        <span class="mr-2 mb-0.2">2</span>
                        <svg data-accordion-icon class="w-3 h-3 rotate-180 shrink-0" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5"/>
                        </svg>
                      </span>
                    </button>
                  </h2>
                  <div id="accordion-open-body-3" class="hidden" aria-labelledby="accordion-open-heading-3">
                    <div class="border border-gray-200 dark:border-gray-700 dark:bg-gray-900">
                      <ul role="list" class="max-w-sm divide-y divide-gray-200 dark:divide-gray-700 border rounded-b-xl">
                          <li class="py-2 sm:py-2">
                              <div class="flex items-center space-x-3 rtl:space-x-reverse">
                                  <div class="flex-shrink-0">
                                  </div>
                                  <div class="flex-1 min-w-0">
                                      <p class="text-sm font-normal text-gray-900 truncate dark:text-white ml-1">
                                          송혜교
                                      </p>
                                      <p class="text-sm text-gray-500 truncate dark:text-gray-400 ml-1">
                                          여 31세
                                      </p>
                                  </div>
                                  <span class="inline-flex items-center text-xs font-medium px-2.5 py-0.5 rounded-full">
                                    <span class="text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-blue-400 border border-blue-400">
                                      진행중
                                    </span>
                                  </span>
                              </div>
                          </li>
                          <li class="py-2 sm:py-2">
                              <div class="flex items-center space-x-3 rtl:space-x-reverse">
                                  <div class="flex-shrink-0">
                                  </div>
                                  <div class="flex-1 min-w-0">
                                      <p class="text-sm font-normal text-gray-900 truncate dark:text-white ml-1">
                                          김메디
                                      </p>
                                      <p class="text-sm text-gray-500 truncate dark:text-gray-400 ml-1">
                                          남 23세
                                      </p>
                                  </div>
                                  <span class="inline-flex items-center text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-red-900 dark:text-red-300">
                                      <span class="text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-gray-700 dark:text-green-400 border border-green-400">
                                        우선대기
                                      </span>
                                  </span>
                              </div>
                          </li>
                      </ul>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>
<!--          <div class="w-160 profile h-screen flex overflow-hidden">-->
<!--          </div>-->
          <div class="flex flex-col w-screen h-screen overflow-hidden bg-white rounded-lg z-5 ml-3 mt-3">
            <header class="inline-flex text-sm text-gray-500 bg-white border border-gray-200 shadow-sm w-full">
              <div role="button" type="button" data-modal-target="p-info-modal" data-modal-toggle="p-info-modal" class="flex flex-row p-3 items-center justify-center border-r-2 border-gray-200 hover:bg-blue-50">
                <div class="flex flex-row">
                    <div class="flex flex-row">
                      <p class="flex flex-row text-sm font-normal items-center">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 18">
                          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm-2 3h4a4 4 0 0 1 4 4v2H1v-2a4 4 0 0 1 4-4Z"/>
                        </svg>
                        <span class="ml-2">113392</span>
                        <a class="ml-1 font-semibold">이수진</a>
                        <span class="ml-1">여 31세 (1993-11-11)</span>
<!--                          <span class="ml-4">-->
<!--                            <button type="button" class="flex flex-row items-center">-->
<!--                              <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">-->
<!--                                <path d="M18 7.5h-.423l-.452-1.09.3-.3a1.5 1.5 0 0 0 0-2.121L16.01 2.575a1.5 1.5 0 0 0-2.121 0l-.3.3-1.089-.452V2A1.5 1.5 0 0 0 11 .5H9A1.5 1.5 0 0 0 7.5 2v.423l-1.09.452-.3-.3a1.5 1.5 0 0 0-2.121 0L2.576 3.99a1.5 1.5 0 0 0 0 2.121l.3.3L2.423 7.5H2A1.5 1.5 0 0 0 .5 9v2A1.5 1.5 0 0 0 2 12.5h.423l.452 1.09-.3.3a1.5 1.5 0 0 0 0 2.121l1.415 1.413a1.5 1.5 0 0 0 2.121 0l.3-.3 1.09.452V18A1.5 1.5 0 0 0 9 19.5h2a1.5 1.5 0 0 0 1.5-1.5v-.423l1.09-.452.3.3a1.5 1.5 0 0 0 2.121 0l1.415-1.414a1.5 1.5 0 0 0 0-2.121l-.3-.3.452-1.09H18a1.5 1.5 0 0 0 1.5-1.5V9A1.5 1.5 0 0 0 18 7.5Zm-8 6a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Z"/>-->
<!--                              </svg>-->
<!--                              <span class="ml-1">정보수정</span>-->
<!--                            </button>-->
<!--                          </span>-->
                      </p>
                    </div>
                </div>
              </div>

              <div class="flex flex-row pt-3 pb-3 items-center justify-center">
                <span class="text-xs pl-3 pr-3 border-r-2">이수진 의사</span>
              </div>
              <div role="button" type="button" data-modal-target="family-list-modal" data-modal-toggle="family-list-modal" class="flex flex-row p-3 items-center justify-center border-gray-200 hover:bg-blue-50">
                <div class="flex flex-row">
                    <div class="flex flex-row">
                      <p class="flex flex-row text-xs font-normal items-center">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                          <path d="M16 0H4a2 2 0 0 0-2 2v1H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v1a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4.5a3 3 0 1 1 0 6 3 3 0 0 1 0-6ZM13.929 17H7.071a.5.5 0 0 1-.5-.5 3.935 3.935 0 1 1 7.858 0 .5.5 0 0 1-.5.5Z"/>
                        </svg>
                        <a class="ml-1 font-semibold">이아들</a>
                        <span class="ml-1">남 11세</span>
<!--                          <span class="ml-4">-->
<!--                            <button type="button" class="flex flex-row items-center">-->
<!--                              <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">-->
<!--                                <path d="M18 7.5h-.423l-.452-1.09.3-.3a1.5 1.5 0 0 0 0-2.121L16.01 2.575a1.5 1.5 0 0 0-2.121 0l-.3.3-1.089-.452V2A1.5 1.5 0 0 0 11 .5H9A1.5 1.5 0 0 0 7.5 2v.423l-1.09.452-.3-.3a1.5 1.5 0 0 0-2.121 0L2.576 3.99a1.5 1.5 0 0 0 0 2.121l.3.3L2.423 7.5H2A1.5 1.5 0 0 0 .5 9v2A1.5 1.5 0 0 0 2 12.5h.423l.452 1.09-.3.3a1.5 1.5 0 0 0 0 2.121l1.415 1.413a1.5 1.5 0 0 0 2.121 0l.3-.3 1.09.452V18A1.5 1.5 0 0 0 9 19.5h2a1.5 1.5 0 0 0 1.5-1.5v-.423l1.09-.452.3.3a1.5 1.5 0 0 0 2.121 0l1.415-1.414a1.5 1.5 0 0 0 0-2.121l-.3-.3.452-1.09H18a1.5 1.5 0 0 0 1.5-1.5V9A1.5 1.5 0 0 0 18 7.5Zm-8 6a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7Z"/>-->
<!--                              </svg>-->
<!--                              <span class="ml-1">정보수정</span>-->
<!--                            </button>-->
<!--                          </span>-->
                      </p>
                    </div>
                </div>
              </div>

            </header>

            <div class="inline-flex flex-row overflow-hidden">
              <div class="sticky h-screen w-60 bg-white border border-gray-200 dark:bg-gray-800 dark:border-gray-700 z-5">
                <div class="pb-2">
                  <div class="sub-menu-p-list">
                    <div class="flex px-4 pt-4 justify-between items-center">
                        <h5 class="ml-1 text-sm font-bold text-gray-600 dark:text-white">내원이력</h5>
                        <button id="dropdownButton" data-dropdown-toggle="dropdown" class="inline-block text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:ring-4 focus:outline-none focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-1.5" type="button">
                            <span class="sr-only">Open dropdown</span>
                            <svg class="w-4 h-4 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                              <path stroke="gray" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 1v3m5-3v3m5-3v3M1 7h18M5 11h10M2 3h16a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1Z"/>
                            </svg>
                        </button>
                        <!-- Dropdown menu -->
                        <div id="dropdown" class="z-10 hidden text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
                            <ul class="py-2" aria-labelledby="dropdownButton">
                            <li>
                                <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Edit</a>
                            </li>
                            <li>
                                <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Export Data</a>
                            </li>
                            <li>
                                <a href="#" class="block px-4 py-2 text-sm text-red-600 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Delete</a>
                            </li>
                            </ul>
                        </div>
                    </div>


                    <div class="mt-4 w-full h-screen text-xs font-medium text-gray-900 bg-white border border-gray-200 rounded-lg dark:bg-gray-700 dark:border-gray-600 dark:text-white">
                        <a href="#" aria-current="true" class="block mb-2 w-full px-4 py-2 text-gray-600 bg-blue-50 border-b border-gray-200 rounded-lg cursor-pointer dark:bg-gray-800 dark:border-gray-600">
                            2022.02.14
                          <span class="inline-flex items-center justify-center w-4 h-4 ms-2 text-xs font-semibold text-blue-800 bg-blue-200 rounded-full">
                          초
                          </span>
                          <span class="inline-flex items-center justify-center w-4 h-4 ml-0.5 text-xs font-semibold text-blue-800 bg-blue-200 rounded-full">
                          주
                          </span>
                        </a>
                        <a href="#" class="block mb-2 w-full px-4 py-2 text-gray-600 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100 hover:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white">
                            2022.02.14
                        </a>
                        <a href="#" class="block mb-2 w-full px-4 py-2 text-gray-600 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100 hover:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white">
                            2022.02.13
                        </a>
                        <a href="#" class="block mb-2 w-full px-4 py-2 text-gray-600 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100 hover:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white">
                            2022.02.11
                        </a>
                    </div>

                  </div>
                </div>
              </div>

              <div class="flex flex-col w-screen h-screen overflow-hidden bg-white rounded-lg z-5 ml-3 mt-3">
                <div class="h-[45%] overflow-hidden">
                    <div class="flex px-1 pt-2 pb-1 justify-between items-center">
                        <h5 class="text-sm font-bold text-gray-600 dark:text-white">2022-02-16 10:16</h5>
                    </div>
                  <div class="flex flex-row w-full h-full">
                    <div class="flex flex-col w-[50%] content-between px-2 mr-3 rounded-lg border border-b-gray-300 h-[85%]">
                      <div class="inline-flex text-sm text-gray-500 bg-white w-full h-10 items-center">
                        <h5 class="ml-1 text-sm font-bold text-gray-600 dark:text-white">진료 기록</h5>
                      </div>
                      <div class="flex flex-col h-full mb-6 justify-between">

                        <p class="flex flex-row ml-1 text-xs font-normal">
                          <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                            <path d="M16 0H4a2 2 0 0 0-2 2v1H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v1a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4.5a3 3 0 1 1 0 6 3 3 0 0 1 0-6ZM13.929 17H7.071a.5.5 0 0 1-.5-.5 3.935 3.935 0 1 1 7.858 0 .5.5 0 0 1-.5.5Z"/>
                          </svg>
                          <a class="ml-1 font-semibold">X-ray 1</a>
                          <span class="ml-1">발목</span>
                          <span class="ml-1">11:06</span>
                          <span class="ml-1"><a href="#">사진</a></span>
                          <span class="ml-1">| 홍길동</span>
                        </p>
                        <div>
                          <button type="button" data-modal-target="treatment-modal" data-modal-toggle="treatment-modal"  class="ml-3 px-5 py-2.5 text-xs font-medium text-white inline-flex items-center bg-[#5A9FFE] hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                            <svg class="w-3 h-3 text-gray-800 dark:text-white mr-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="white" viewBox="0 0 20 20">
                              <path d="m13.835 7.578-.005.007-7.137 7.137 2.139 2.138 7.143-7.142-2.14-2.14Zm-10.696 3.59 2.139 2.14 7.138-7.137.007-.005-2.141-2.141-7.143 7.143Zm1.433 4.261L2 12.852.051 18.684a1 1 0 0 0 1.265 1.264L7.147 18l-2.575-2.571Zm14.249-14.25a4.03 4.03 0 0 0-5.693 0L11.7 2.611 17.389 8.3l1.432-1.432a4.029 4.029 0 0 0 0-5.689Z"/>
                            </svg>
                            진료기록 추가
                          </button>
                        </div>
                      </div>





                    </div>
                    <div class="flex flex-col w-[50%] content-between px-2 mr-3 rounded-lg border border-b-gray-300 h-[85%]">
                      <div class="inline-flex text-sm text-gray-500 bg-white w-full h-10 items-center">
                        <h5 class="ml-1 text-sm font-bold text-gray-600 dark:text-white">검사 기록</h5>
                      </div>
                      <div class="grid gap-6 mb-6 md:grid-cols-2 h-full">
                        <div class="flex flex-col h-full justify-between">
                          <p class="flex flex-row ml-1 text-xs font-normal">
                            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                              <path d="M16 0H4a2 2 0 0 0-2 2v1H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v1a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4.5a3 3 0 1 1 0 6 3 3 0 0 1 0-6ZM13.929 17H7.071a.5.5 0 0 1-.5-.5 3.935 3.935 0 1 1 7.858 0 .5.5 0 0 1-.5.5Z"/>
                            </svg>
                            <a class="ml-1 font-semibold">X-ray 1</a>
                            <span class="ml-1">발목</span>
                            <span class="ml-1">11:06</span>
                            <span class="ml-1"><a href="#">사진</a></span>
                            <span class="ml-1">| 홍길동</span>
                          </p>
                          <div>
                            <button type="button" data-modal-target="x-ray-modal" data-modal-toggle="x-ray-modal"  class="ml-3 px-5 py-2.5 text-xs font-medium text-white inline-flex items-center bg-[#5A9FFE] hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                              <svg class="w-3 h-3 text-gray-800 dark:text-white mr-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="white" viewBox="0 0 20 20">
                                <path d="m13.835 7.578-.005.007-7.137 7.137 2.139 2.138 7.143-7.142-2.14-2.14Zm-10.696 3.59 2.139 2.14 7.138-7.137.007-.005-2.141-2.141-7.143 7.143Zm1.433 4.261L2 12.852.051 18.684a1 1 0 0 0 1.265 1.264L7.147 18l-2.575-2.571Zm14.249-14.25a4.03 4.03 0 0 0-5.693 0L11.7 2.611 17.389 8.3l1.432-1.432a4.029 4.029 0 0 0 0-5.689Z"/>
                              </svg>
                              X-ray 추가
                            </button>
                          </div>
                        </div>
                        <div class="flex flex-col h-full justify-between">
                          <div class="flex flex-col ml-1 text-xs font-normal">
                            <div class="flex flex-row">
                              <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                                <path d="M16 0H4a2 2 0 0 0-2 2v1H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v2H1a1 1 0 0 0 0 2h1v1a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4.5a3 3 0 1 1 0 6 3 3 0 0 1 0-6ZM13.929 17H7.071a.5.5 0 0 1-.5-.5 3.935 3.935 0 1 1 7.858 0 .5.5 0 0 1-.5.5Z"/>
                              </svg>
                              <a class="ml-1 font-semibold">InBody</a>
                            </div>
                            <span class="ml-1">체중 74kg</span>
                            <span class="ml-1">체지방률 20%</span>
                            <span class="ml-1">근육량 45%</span>
                            <span class="ml-1">기초대사량 1800kal</span>
                            <span class="ml-1">비만도지수 21kg/m^2</span>
                            <span class="ml-1">수분함량 55%</span>
                          </div>
                          <div>
                            <button type="button" data-modal-target="inbody-modal" data-modal-toggle="inbody-modal" class="ml-3 px-5 py-2.5 text-xs font-medium text-white inline-flex items-center bg-[#5A9FFE] hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                              <svg class="w-3 h-3 text-gray-800 dark:text-white mr-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="white" viewBox="0 0 20 20">
                                <path d="m13.835 7.578-.005.007-7.137 7.137 2.139 2.138 7.143-7.142-2.14-2.14Zm-10.696 3.59 2.139 2.14 7.138-7.137.007-.005-2.141-2.141-7.143 7.143Zm1.433 4.261L2 12.852.051 18.684a1 1 0 0 0 1.265 1.264L7.147 18l-2.575-2.571Zm14.249-14.25a4.03 4.03 0 0 0-5.693 0L11.7 2.611 17.389 8.3l1.432-1.432a4.029 4.029 0 0 0 0-5.689Z"/>
                              </svg>
                              Inbody 기록
                            </button>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="h-[45%]">
                  <div class="flex flex-col content-between px-2 mr-3 justify-between rounded-lg border border-b-gray-300 h-[85%]">
                    <div class="inline-flex text-sm text-gray-500 bg-white w-full h-10 items-center">
                      <h5 class="ml-1 text-sm font-bold text-gray-600 dark:text-white">진단 및 처방</h5>
                    </div>
                    <div>
                      <div class="mb-3">
                        <button type="button" data-modal-target="prescription-modal" data-modal-toggle="prescription-modal"  class="ml-3 px-5 py-2.5 text-xs font-medium text-white inline-flex items-center bg-[#5A9FFE] hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                          <svg class="w-3 h-3 text-gray-800 dark:text-white mr-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="white" viewBox="0 0 20 20">
                            <path d="m13.835 7.578-.005.007-7.137 7.137 2.139 2.138 7.143-7.142-2.14-2.14Zm-10.696 3.59 2.139 2.14 7.138-7.137.007-.005-2.141-2.141-7.143 7.143Zm1.433 4.261L2 12.852.051 18.684a1 1 0 0 0 1.265 1.264L7.147 18l-2.575-2.571Zm14.249-14.25a4.03 4.03 0 0 0-5.693 0L11.7 2.611 17.389 8.3l1.432-1.432a4.029 4.029 0 0 0 0-5.689Z"/>
                          </svg>
                          진단 및 처방 추가
                        </button>
                      </div>
                  <footer class="flex space-between bg-white rounded-lg shadow border border-gray-100 dark:bg-gray-800">
                    <div class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center md:justify-between">
                      <span class="flex flex-row items-center text-sm text-gray-500 sm:text-center dark:text-gray-400">
                        <svg class="w-3 h-3 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                          <path stroke="gray" stroke-linejoin="round" stroke-width="2" d="M8 8v1h4V8m4 7H4a1 1 0 0 1-1-1V5h14v9a1 1 0 0 1-1 1ZM2 1h16a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1Z"/>
                        </svg>
                        <a class="ml-1">
                        진료실01
                        </a>
                      </span>
                      <div class="mx-6"></div>
                      <div class="flex flex-row">
                        <select id="countries" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-22 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                          <option value="US" selected>수납실</option>
                          <option value="CA">검사실</option>
                          <option value="FR">입원실</option>
                          <option value="DE">운동치료실</option>
                          <option value="DE">작업치료실</option>
                        </select>

                        <select id="countries" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-400 block w-20 p-2.5 dark:bg-gray-600 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                          <option value="US" selected>대기</option>
                          <option value="US">우선대기</option>
                          <option value="CA">진행중</option>
                          <option value="FR">완료</option>
                        </select>

                        <button type="button" class="ml-3 px-5 py-2.5 text-sm font-medium text-white inline-flex items-center bg-[#5A9FFE] hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                          <svg class="rotate-90 mr-3 w-3 h-3 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="white" viewBox="0 0 18 20">
                            <path d="m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z"/>
                          </svg>
                          보내기
                        </button>
                      </div>

                    </div>
                </footer>
                    </div>
                  </div>
                </div>
              </div>


            </div>






          </div>


        </div>
      </div>
    </div>
  </body>
</template>

<style scoped>
:root {
  --c-text-primary: #282a32;
  --c-text-secondary: #686b87;
  --c-text-action: #404089;
  --c-accent-primary: #434ce8;
  --c-border-primary: #eff1f6;
  --c-background-primary: #ffffff;
  --c-background-secondary: #fdfcff;
  --c-background-tertiary: #ecf3fe;
  --c-background-quaternary: #e9ecf4;
}


html, body {
  line-height: 1.5;
  font-family: 'Noto Sans KR', sans-serif;
  background-color: var(--c-background-secondary);
  color: var(--c-text-primary);
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: static;
  padding: 0;
  margin: 0;
}

img {
  display: block;
  max-width: 100%;
}

header {
  display: flex;
  align-content: center;
  height: 58px;
  background-color: white;
}

:focus {
  outline: 0;
}

.responsive-wrapper {
  width: 100%;
  height: 84vh;
  margin-inline: auto;
  overflow: hidden;
}

.sidebar {
  flex-wrap: wrap;
}

.sidebar-login {
    padding-top: 26rem;
}

@media (min-width: 640px) {
  .sidebar {

  }
}

.header {
  display: flex;
  align-items: center;
  height: 80px;
  border-bottom: 1px solid var(--c-border-primary);
  background-color: var(--c-background-primary);
  overflow: hidden;
}

.header-content {
  width: 100%;
  display: flex;
  align-items: flex-start;
  margin-left: 0.75rem;
  margin-right: 0.75rem;
}
.header-content > a {
  display: none;
}
@media (max-width: 1200px) {
  .header-content {
    justify-content: space-between;
  }
  .header-content > a {
    display: inline-flex;
  }
}

.header-title {
  display: flex;
  margin-right: 2.5rem;
}

.header-logo {
  margin-right: 0.75rem;
}
.header-logo a {
  display: flex;
  align-items: center;
}
.header-logo a div {
  flex-shrink: 0;
  position: relative;
}
.header-logo a div:after {
  display: block;
  content: "";
  position: absolute;
  left: 0;
  top: auto;
  right: 0;
  bottom: 0;
  overflow: hidden;
  height: 50%;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  background-color: rgba(255, 255, 255, 0.2);
  -webkit-backdrop-filter: blur(4px);
          backdrop-filter: blur(4px);
}

.header-name {
  font-size: 1.3em;
  font-weight: 700;
  align-items: center;
}

.header-navigation {
  display: flex;
  flex-grow: 1;
  align-items: center;
  justify-content: space-between;
}

.content-header {
}

@media (max-width: 1200px) {
  .header-navigation {
    display: none;
  }
  .header-title {
    margin-left: 0.75em;
  }
}

.header-navigation-actions {
  display: flex;
  align-items: center;
}
.header-navigation-actions > .avatar {
  margin-left: 0.75rem;
}
.header-navigation-actions > .icon-button + .icon-button {
  margin-left: 0.25rem;
}
.header-navigation-actions > .button + .icon-button {
  margin-left: 1rem;
}

.button {
  font: inherit;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0 1em;
  height: 40px;
  border-radius: 8px;
  line-height: 1;
  border: 2px solid var(--c-border-primary);
  color: var(--c-text-action);
  font-size: 0.875rem;
  transition: 0.15s ease;
  background-color: var(--c-background-primary);
}
.button i {
  margin-right: 0.5rem;
  font-size: 1.25em;
}
.button span {
  font-weight: 500;
}
.button:hover, .button:focus {
  border-color: var(--c-accent-primary);
  color: var(--c-accent-primary);
}

.icon-button {
  font: inherit;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 8px;
  color: var(--c-text-action);
  transition: 0.15s ease;
}
.icon-button i {
  font-size: 1.25em;
}
.icon-button:focus, .icon-button:hover {
  background-color: var(--c-background-tertiary);
  color: var(--c-accent-primary);
}


.search-input {

}

.title {
  font-family: 'Righteous', sans-serif;
}



.avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  overflow: hidden;
}

.main {
  background-color: rgb(244, 244, 244);
  width: 100%;
  height: 100%;
  margin-inline: auto;
}

.title {
  font-family: 'Righteous', sans-serif;
}

.sidebar-home {
}

.search {
  position: relative;
  display: flex;
  align-items: center;
  margin: 0 auto;
  width: 100%;
  max-width: 498px;
}
.search input {
  font: inherit;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0 1em 0 36px;
  height: 35px;
  border-radius: 8px;
  border: 2px solid var(--c-border-primary);
  color: var(--c-text-action);
  font-size: 0.775rem;
  transition: 0.15s ease;
  width: 100%;
  line-height: 1;
  background-color: #F4F4F4;
  text-align: center;
}
.search input::-moz-placeholder {
  color: var(--c-text-action);
}
.search input:-ms-input-placeholder {
  color: var(--c-text-action);
}
.search input::placeholder {
  color: var(--c-text-action);
}
.search input:focus, .search input:hover {
  border-color: var(--c-accent-primary);
}
.search button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 0;
  background-color: transparent;
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.25em;
  color: var(--c-text-action);
  padding: 0;
  height: 40px;
}

.content-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  margin-top: -1px;
  border-top: 1px solid var(--c-border-primary);
}

.content-header-intro h2 {
  font-size: 1.25rem;
  font-weight: 600;
}
.content-header-intro p {
  color: var(--c-text-secondary);
  margin-top: 0.25rem;
  font-size: 0.875rem;
  margin-bottom: 1rem;
}

@media (min-width: 800px) {
  .content-header-actions a:first-child {
    display: none;
  }
}

.content {
  width: 100%;
  height: 100%;
  border-top: 1px solid var(--c-border-primary);
  display: flex;
  align-items: flex-start;
  margin-inline: auto;
}

.content-main {
  width: 100%;
  height: 100%;
  flex-grow: 1;
  margin-inline: auto;
}

.content-grid {
  display: grid;
  width: 100%;
  height: 100%;
  flex-grow: 1;
  grid-template-columns: repeat(2, 1fr);
  padding: 0.75rem;
  justify-content: space-between;
  gap: 0.75rem;
  margin-inline: auto;
}

.left-content {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  column-gap: 1rem;
}

.treatment-bar {
  width: 100%;
  height: 30px;
  display: flex;
  align-items: center;
  margin-bottom: 0.35rem;
  justify-content: space-between;
}

.button-group {
  display: inline-flex;
}

.button-page{
  display: flex;
  align-items: center;
  align-self: center;
  background-color: white;
  border: 2px solid #767577;
  padding: 0.5rem;
  text-transform: none;
}

.button-page :hover{
}



.button-page svg {
  padding: 0;
  margin: 0;
  color: #767577;
}

.page-number {
  display: flex;
  margin-left: 0.75rem;
  margin-right: 0.75rem;
  font-weight: 400;
  color: #777679;
  font-size: 0.8em;
  align-items: center;
  margin-bottom: 0.2rem;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  -moz-column-gap: 0.75rem;
       column-gap: 0.75rem;
  row-gap: 0.75rem;
  flex-grow: 1;
}
@media (min-width: 600px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (min-width: 1200px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

.card {
  background-color: #FFFFFF;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  flex-direction: column;
  padding: 0.5rem 1.25rem 0 0.75rem;
  background-color: #F8F8F8;
  font-size: 0.875rem;
}
.card-header div {
  display: flex;
  align-items: center;
}
.number-wait {
  border-style: solid;
  border-width: 2px;
  border-color: #E2E2E2 #E2E2E2 white #E2E2E2;
}

.card-header div span {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  display: inline-flex;
  align-items: center;
}
.card-header div span img {
  max-height: 100%;
}
.card-header div h3 {
  font-weight: 500;
  padding-bottom: 1rem;
}

.toggle span {
  display: block;
  width: 40px;
  height: 24px;
  border-radius: 99em;
  background-color: var(--c-background-quaternary);
  box-shadow: inset 1px 1px 1px 0 rgba(0, 0, 0, 0.05);
  position: relative;
  transition: 0.15s ease;
}
.toggle span:before {
  content: "";
  display: block;
  position: absolute;
  left: 3px;
  top: 3px;
  height: 18px;
  width: 18px;
  background-color: var(--c-background-primary);
  border-radius: 50%;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.15);
  transition: 0.15s ease;
}
.toggle input {
  clip: rect(0 0 0 0);
  height: 1px;
  overflow: hidden;
  position: absolute;
  white-space: nowrap;
  width: 1px;
}
.toggle input:checked + span {
  background-color: var(--c-accent-primary);
}
.toggle input:checked + span:before {
  transform: translateX(calc(100% - 2px));
}
.toggle input:focus + span {
  box-shadow: 0 0 0 4px var(--c-background-tertiary);
}

.card-body {
  padding: 0;
  font-size: 0.875rem;
}

.card-footer {
  margin-top: auto;
  padding: 1rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  border-top: 1px solid var(--c-border-primary);
}
.card-footer a {
  color: var(--c-text-action);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.875rem;
}



.search-drop-button {
  display: inline-flex;
  align-items: center;
  z-index: 1;
  border-radius: 0.5rem;
  border: 1.5px solid #E2E2E4;
  --tw-bg-opacity: 1;
  background-color: #F9F9F9;
  padding-top: 0.325rem;
  padding-bottom: 0.325rem;
  text-align: center;
  font-size: 0.875rem;
  line-height: 1.25rem;
  font-weight: 500;
  color: #303032;
}

.search-drop-button span {
  margin-left: 0.75rem;
}

.search-drop-button svg {
  margin-right: 0.75rem;
}

html::-webkit-scrollbar {
  width: 12px;
}
html::-webkit-scrollbar-thumb {
  background-color: var(--c-text-primary);
  border: 4px solid var(--c-background-primary);
  border-radius: 99em;
}

.profile {
  display: flex;
  height: 100%;
  position: relative;
  z-index: 2;
}

.text-settings {
  font-size: 0.8rem;
}

.search-bar {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
}

.search-bar form button {
}

.text-sky-blue {
  color: #5A9FFE;
}

.border-sky {
  border-bottom-width: 3px;
  border-bottom-color: #5A9FFE;
}

.patient-list-cards {
  height: 100%;
  align-items: stretch;
  position: relative;
}


.fix-element {
  position: fixed;
}

.sub-chart-bar {
  z-index: 0;
  position: static;
}

.main-bar {
  z-index: 0;
}

.sub-menu-p-list {
  background-color: white;
}

.patient-num-each {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.modal {
  z-index: 100;
}

.bg-sky-blue {
  background-color: #5A9FFE;
}


.content-grid-textbox{
  width: 95%;
  height: 170px;
  margin-top: 0.5rem;
  margin-left: 0.75rem;
  border: 1.5px solid #E2E2E2;
  border-radius: 5px;
  resize: none;
}

</style>

