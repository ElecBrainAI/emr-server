<script setup>
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'
import 'https://unpkg.com/phosphor-icons';
import { FwbButton } from 'flowbite-vue'

import SideBar from "../Components/SideBar.vue";


onMounted(() => {
    initFlowbite();
})

</script>

<template>
  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lilita+One&family=Righteous&family=Song+Myung&family=Varela+Round&display=swap" rel="stylesheet">
    <title></title>
  </head>
  <body>
    <div class="h-screen flex overflow-hidden">
      <!-- SIDEBAR -->
      <div class="w-64 py-4 px-8 bg-gray-100 border-r overflow-auto">
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
                <a href="#" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
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
                  <a href="#" class="text-lg font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white">홈</a>
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
  height: 84vh;
  margin-inline: auto;
  overflow: hidden;
}

.sidebar {
  flex-wrap: wrap;
}


.title {
  font-family: 'Righteous', sans-serif;
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

.header-navigation {
  display: flex;
  flex-grow: 1;
  align-items: center;
  justify-content: space-between;
}

.sub-chart-bar {
  z-index: 0;
  position: static;
}

header {
  display: flex;
  align-content: center;
  height: 58px;
  background-color: white;
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
  background-color: #E7EDF5;
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
  background-color: var(--c-background-secondary);
  width: 100%;
  height: 100%;
  margin-inline: auto;
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

</style>

