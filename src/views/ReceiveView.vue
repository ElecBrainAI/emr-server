<script setup>

import {FwbButton} from "flowbite-vue";
</script>

<template>
  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lilita+One&family=Righteous&family=Song+Myung&family=Varela+Round&display=swap" rel="stylesheet">
  </head>

  <body>
    <div class="h-screen flex overflow-hidden">
      <!-- SIDEBAR -->
      <div class="w-48 py-4 px-8 bg-gray-100 border-r overflow-auto">
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
                <a href="/patient" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
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
                <a href="#" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
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
                  <a href="#" class="text-lg font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white">수납</a>
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
        <div class="inline-flex flex-row overflow-hidden h-full">
          <div class="flex flex-col flex-1 min-w-0 bg-white overflow-hidden h-full">

            <main class="main h-full">
              <div class="responsive-wrapper h-full">
                <div class="content h-full">
                  <div class="content-grid">
                    <div class="content-grid-upper">
                      <span class="content-grid-upper-title">수납</span>

                    </div>
                    <div class="content-grid-main">
                      <div class="content-grid-main-information">
                        <div class="content-grid-main-information-upper">
                          <span class="content-grid-main-information-upper-name">이수진</span>
                          <span class="content-grid-main-information-upper-number">cn.1</span>
                        </div>
                        <div class="content-grid-main-information-lower">
                          <span class="content-grid-main-information-lower-1">881224-2******</span>
                          <span class="content-grid-main-information-lower-2">34세</span>
                          <span class="content-grid-main-information-lower-2">여</span>
                          <span class="content-grid-main-information-lower-2">010-0000-0000</span>
                        </div>

                      </div>
                      <div class="content-grid-main-1">
                          <button class="search-drop-button-1" id="dropdownSearchButton" data-dropdown-toggle="dropdownSearch-1" data-dropdown-placement="bottom" type="button">
                            <span>카드</span>
                            <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
                            </svg>
                          </button>

                          <!-- Dropdown menu -->
                          <div id="dropdownSearch-1" class="z-10 hidden bg-white rounded-lg shadow w-60 dark:bg-gray-700">
                              <div class="p-3">
                                <label for="input-group-search" class="sr-only">Search</label>
                                <div class="relative">
                                  <div class="absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none">
                                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                                    </svg>
                                  </div>
                                  <input type="text" id="input-group-search" class="block w-full p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="진료실 검색">
                                </div>
                              </div>
                              <ul class="h-treatment-1 px-3 pb-3 overflow-y-auto text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownSearchButton">
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                      <input checked id="checkbox-item-reception-5" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                      <label for="checkbox-item-reception-5" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">카드</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">현금</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">미수</label>
                                  </div>
                                </li>



                              </ul>

                          </div>
                      <div class="content-grid-main-1-1">
                        <span class="content-grid-main-text-black">수납금액</span>
                        <input type="text" class="content-grid-main-1-tb" style="text-align: right">

                        <span class="content-grid-main-text-black">할부기간</span>
                        <button class="search-drop-button-2" id="dropdownSearchButton" data-dropdown-toggle="dropdownSearch-2" data-dropdown-placement="bottom" type="button">
                            <span>일시불</span>
                            <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
                            </svg>
                          </button>

                          <!-- Dropdown menu -->
                          <div id="dropdownSearch-2" class="z-10 hidden bg-white rounded-lg shadow w-60 dark:bg-gray-700">
                              <div class="p-3">
                                <label for="input-group-search" class="sr-only">Search</label>
                                <div class="relative">
                                  <div class="absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none">
                                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                                    </svg>
                                  </div>
                                  <input type="text" id="input-group-search" class="block w-full p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="진료실 검색">
                                </div>
                              </div>
                              <ul class="h-treatment-1 px-3 pb-3 overflow-y-auto text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownSearchButton">
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                      <input checked id="checkbox-item-reception-5" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                      <label for="checkbox-item-reception-5" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">일시불</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">1개월</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">2개월</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">3개월</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">4개월</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">5개월</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">6개월</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">7개월</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">8개월</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">9개월</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">10개월</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">11개월</label>
                                  </div>
                                </li>
                                <li>
                                  <div class="flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                    <input id="checkbox-item-reception-6" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                                    <label for="checkbox-item-reception-6" class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">12개월</label>
                                  </div>
                                </li>




                              </ul>

                          </div>

                      </div>


                      </div>
                      <div class="content-grid-main-2">
                        <div class="content-grid-main-2-1">
                          <span class="content-grid-main-text-black">총진료비</span>
                          <input type="text" class="content-grid-main-1-tb2" style="text-align: right">
                        </div>
                        <div class="underbar"></div>
                        <div class="content-grid-main-2-2">
                          <span class="content-grid-main-text-black">본인부담금</span>
                          <input type="text" class="content-grid-main-1-tb3" style="text-align: right">
                        </div>
                        <span class="content-grid-main-2-text">(공단부담금: 11,970원)</span>
                        <div class="content-grid-main-2-3">
                          <span class="content-grid-main-text-black">비급여</span>
                          <input type="text" class="content-grid-main-1-tb4" style="text-align: right">
                        </div>

                      </div>
                    </div>
                    <div class="content-grid-lower">
                      <div class="content-grid-lower-1">
                        <span class="content-grid-main-text-black">수납할 금액</span>
                        <div>
                          <input type="text" class="content-grid-lower-1-tb" style="text-align: right">
                          <span class="content-grid-main-text-black">원</span>
                        </div>

                      </div>
                      <div class="content-grid-lower-2">
                        <div class="content-grid-lower-2-group">
                          <div class="content-grid-lower-2-group-box flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                            <input checked id="checkbox-item-reception-1" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                            <label for="checkbox-item-reception-1" class="content-grid-lower-2-group-text w-full py-2 ms-2 text-sm  text-gray-900 rounded dark:text-gray-300">진료비영수증</label>
                          </div>
                          <div class="content-grid-lower-2-group-box flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                            <input checked id="checkbox-item-reception-1" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                            <label for="checkbox-item-reception-1" class="content-grid-lower-2-group-text w-full py-2 ms-2 text-sm  text-gray-900 rounded dark:text-gray-300">진료비세부산정내역</label>
                          </div>
                          <div class="content-grid-lower-2-group-box flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                            <input checked id="checkbox-item-reception-1" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                            <label for="checkbox-item-reception-1" class="content-grid-lower-2-group-text w-full py-2 ms-2 text-sm  text-gray-900 rounded dark:text-gray-300">처방전</label>
                          </div>
                          <div class="content-grid-lower-2-group-box flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                            <input checked id="checkbox-item-reception-1" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500">
                            <label for="checkbox-item-reception-1" class="content-grid-lower-2-group-text w-full py-2 ms-2 text-sm  text-gray-900 rounded dark:text-gray-300">미출력 서류</label>
                          </div>
                        </div>
                        <button class="styled-b" type="button">수납</button>
                      </div>

                    </div>
                  </div>

                </div>
              </div>
            </main>
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
  position: fixed;
  padding: 0;
  margin: 0;
}

img {
  display: block;
  max-width: 100%;
}

:focus {
  outline: 0;
}

.responsive-wrapper {
  width: 100%;
  height: 100%;
  margin-inline: auto;
  overflow: hidden;
}

.sidebar {
  flex-wrap: wrap;
}

.sidebar-login {
  padding-top: 26rem;
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

header {
  display: flex;
  align-content: center;
  height: 58px;
  background-color: white;
}


.sub-chart-bar {
  z-index: 0;
  position: static;
}

.header-navigation {
  display: flex;
  flex-grow: 1;
  align-items: center;
  justify-content: space-between;
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
  background-color: #767577;
  width: 100%;
  height: 100%;
  margin-inline: auto;
}

.title {
  font-family: 'Righteous', sans-serif;
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
  align-items: center;
  margin-inline: auto;
}

.content-grid {
  width: 600px;
  height: 95%;
  background-color: #FFFFFF;
  border-radius: 7px;
  display: flex;
  align-items: center;
  flex-direction: column;
  margin: 0 auto;
}

.content-grid-upper {
  width: 100%;
  height: 10%;
  display: flex;
  align-items: center;
  background-color: #F2F2F4;
  border: 1px solid #E2E2E2;
}

.content-grid-upper-title{
  width: 100%;
  color: #111827;
  margin-left: 0.75rem;
  margin-right: 1rem;
  font-size: 0.9rem;
  font-weight: bold;
}





.content-grid-main {
  width: 100%;
  height: 70%;
  display: flex;
  align-items: center;
  flex-direction: column;
}

.content-grid-main-information {
  width: 100%;
  height: 50px;
  background-color: #FFFFFF;
  border-radius: 7px;
  display: flex;
  align-items: center;
  margin-bottom: 0.35rem;
  flex-direction: column;
  margin-right: auto;
}

.content-grid-main-information-upper {
  width: 100%;
  height: 60%;
  display: flex;
  flex-direction: row;

}

.content-grid-main-information-upper-name{
  color: #111827;
  margin-top: 0.5rem;
  margin-left: 0.75rem;
  margin-right: 1rem;
  font-size: 0.9rem;
  font-weight: bold;
}

.content-grid-main-information-upper-number{
  color: #111827;
  margin-top: 0.5rem;
  font-size: 0.75rem;
  font-weight: bold;
}

.content-grid-main-information-lower {
  width: 100%;
  height: 40%;
  display: flex;
  flex-direction: row;
}

.content-grid-main-information-lower-1{
  color: #767577;
  margin-left: 0.75rem;
  margin-right: 1.5rem;
  font-size: 0.8rem;
  font-weight: bold;
}

.content-grid-main-information-lower-2{
  color: #767577;
  margin-right: 0.5rem;
  font-size: 0.8rem;
  font-weight: bold;
}

.content-grid-main-1{
  width: 85%;
  height: 120px;
  border-radius: 7px;
  display: flex;
  align-items: center;
  flex-direction: column;
  background-color: #F2F2F4;
}

.search-drop-button-1 {
  width: 150px;
  display: inline-flex;
  justify-content: space-between;
  align-items: center;
  z-index: 1;
  border-radius: 0.5rem;
  border: 1.5px solid #E2E2E4;
  --tw-bg-opacity: 1;
  background-color: #FFFFFF;
  padding-top: 0.325rem;
  padding-bottom: 0.325rem;
  text-align: center;
  font-size: 0.875rem;
  line-height: 1.25rem;
  font-weight: 500;
  color: #303032;
  margin-left: 1rem;
  margin-right: auto;
  margin-top: 0.5rem;
}

.search-drop-button-1 span {
  margin-left: 0.75rem;
}

.search-drop-button-1 svg {
  margin-right: 0.75rem;
}

.content-grid-main-1-1{
  width: 100%;
  height: 50px;
  border-radius: 7px;
  display: flex;
  align-items: center;
  flex-direction: row;
  margin-top: 1rem;
  justify-content: space-between;
}

.content-grid-main-1-tb{
  width: 150px;
  height: 30px;
  border-radius: 0.5rem;
  border: 1.5px solid #E2E2E4;
  margin-left: 1rem;
  margin-right: 1rem;
}

.search-drop-button-2 {
  width: 150px;
  display: inline-flex;
  justify-content: space-between;
  align-items: center;
  z-index: 1;
  border-radius: 0.5rem;
  border: 1.5px solid #E2E2E4;
  --tw-bg-opacity: 1;
  background-color: #FFFFFF;
  padding-top: 0.325rem;
  padding-bottom: 0.325rem;
  text-align: center;
  font-size: 0.875rem;
  line-height: 1.25rem;
  font-weight: 500;
  color: #303032;
  margin-left: 1rem;
  margin-right: auto;
}

.search-drop-button-2 span {
  margin-left: 0.75rem;
}

.search-drop-button-2 svg {
  margin-right: 0.75rem;
}

.content-grid-main-2{
  width: 85%;
  height: 200px;
  border-radius: 7px;
  display: flex;
  align-items: center;
  flex-direction: column;
  background-color: #F2F2F4;
  margin-top: 1rem;
}

.content-grid-main-2-1{
  width: 90%;
  height: 35px;
  display: flex;
  align-items: center;
  flex-direction: row;
  margin-top: 1rem;
  justify-content: space-between;

}

.content-grid-main-1-tb2{
  width: 200px;
  height: 30px;
  border-radius: 0.5rem;
  border: 1.5px solid #E2E2E4;
  margin-right: 6rem;
}

.underbar{
  width: 90%;
  height: 2px;
  background-color: #D9D9D9;
  margin-top: 0.5rem;
}
.content-grid-main-2-2{
  width: 90%;
  height: 35px;
  display: flex;
  align-items: center;
  flex-direction: row;
  margin-top: 1rem;
  justify-content: space-between;
}

.content-grid-main-1-tb3{
  width: 200px;
  height: 30px;
  border-radius: 0.5rem;
  border: 1.5px solid #E2E2E4;
  margin-right: 6rem;
}

.content-grid-main-2-text{
  color: #111827;
  font-size: 0.7rem;
  font-weight: bold;
  margin-left: auto;
  margin-right: 8rem;
}

.content-grid-main-2-3{
  width: 90%;
  height: 35px;
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
}

.content-grid-main-1-tb4{
  width: 200px;
  height: 30px;
  border-radius: 0.5rem;
  border: 1.5px solid #E2E2E4;
  margin-right: 6rem;
}


.content-grid-main-text-black{
  color: #111827;
  margin-left: 0.75rem;
  font-size: 0.85rem;
  font-weight: bold;
}



.h-treatment-1 {
  height: 7.5rem/* 192px */;
}

.h-treatment-2 {
  height: 5rem/* 192px */;
}






.content-grid-lower {
  width: 100%;
  height: 20%;
  display: flex;
  padding-left: 0.75rem;
  padding-right: 0.75rem;
  align-items: center;
  justify-content: space-between;
  border: 1.5px solid #E2E2E2;
  flex-direction: column;
}

.content-grid-lower-1 {
  width: 90%;
  height: 40%;
  display: flex;
  padding-left: 0.75rem;
  padding-right: 0.75rem;
  align-items: center;
  justify-content: space-between;
}

.content-grid-lower-1-tb{
  width: 300px;
  height: 35px;
  border-radius: 0.5rem;
  border: 1.5px solid #E2E2E4;
}

.content-grid-lower-2 {
  width: 90%;
  height: 60%;
  display: flex;
  padding-left: 0.75rem;
  padding-right: 0.75rem;
  align-items: center;
  justify-content: space-between;
}

.content-grid-lower-2-group{
  width: 70%;
  height: 100%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-content: center;
}

.content-grid-lower-2-group-box{
  height: 25px;
}

.content-grid-lower-2-group-text{
  color: #111827;
  font-size: 0.75rem;
  font-weight: bold;
  padding-top: 0rem;
  padding-bottom: 0rem;
}

.styled-w {
  line-height: 2.5;
  padding: 0 20px;
  font-size: 1rem;
  text-align: center;
  color: #111827;
  border-radius: 20px;
  background-color: #FFFFFF;
  border: 1.5px solid #E2E2E2;
}

.styled-b {
  border: 0;
  line-height: 2.5;
  padding: 0 30px;
  font-size: 1rem;
  text-align: center;
  color: #fff;
  border-radius: 20px;
  background-color: #335ACA;
}

.styled-b:active {

    box-shadow: inset -.1rem -.1rem 1.4rem  #434ce8, inset .1rem .2rem .4rem #303032;
    cursor: pointer;

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
  width: 230px;
  display: inline-flex;
  justify-content: space-between;
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

</style>