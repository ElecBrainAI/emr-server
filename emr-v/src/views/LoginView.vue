<script setup>
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'
import 'https://unpkg.com/phosphor-icons';

onMounted(() => {
    initFlowbite();
})


</script>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        // axios 또는 fetch를 사용하여 백엔드로 로그인 정보를 전송
        const response = await axios.post('https://port-0-emr-server-5mk12alph04yvt.sel5.cloudtype.app/patman/sign_in/', {
          username: this.username,
          password: this.password
        });
        console.log(response.data); // 서버에서 받은 응답 확인
        this.$router.push('/');
        // 성공적으로 로그인했을 때의 처리
      } catch (error) {
        console.error('로그인 에러:', error);
        this.$router.push('/login');
        // 로그인 실패 또는 에러 처리
      }
    }
  }
};
</script>

<template>
  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lilita+One&family=Righteous&family=Song+Myung&family=Varela+Round&display=swap" rel="stylesheet">
    <title></title>
  </head>
  <body>
    <div class="login">
      <header>

      </header>
      <main class="main">
        <div class="container">
          <div class="row">
            <div class="Absolute-Center is-Responsive">
              <div id="logo-container">
                EMR
              </div>
              <div id="login-input" class="login-input col-sm-12 col-md-10 col-md-offset-1">
                <div id="login-userid" class="relative mb-2">
                  <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 14 18">
                      <path d="M7 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9Zm2 1H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z"/>
                    </svg>
                  </div>
                  <input type="text" v-model ="username" id="input-group-1" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="사용자이름">
                </div>
                <div id="login-pw" class="relative mb-2">
                  <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 16 20">
                      <path d="M14 7h-1.5V4.5a4.5 4.5 0 1 0-9 0V7H2a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2Zm-5 8a1 1 0 1 1-2 0v-3a1 1 0 1 1 2 0v3Zm1.5-8h-5V4.5a2.5 2.5 0 1 1 5 0V7Z"/>
                    </svg>
                  </div>
                  <input type="text" v-model="password" id="input-group-1" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="비밀번호">
                </div>
              </div>
              <div class="login-middle flex items-center">
                <div class="login-middle flex items-center mb-4">
                  <div class="button-selectId">
                    <input id="default-checkbox" type="checkbox" value="" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded">
                    <label for="default-checkbox" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">ID 저장</label>
                  </div>
                  <label for="link-radio" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"><a href="#" class="text-blue-600 dark:text-blue-500">비밀번호를 잊으셨나요?</a></label>
                </div>
              </div>
              <div class="login-bottom">
                <button type="button" @click=login  class="login-button text-white hover:bg-blue-600 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">로그인</button>
                <button type="button" onclick="location.href='/signup'" class="signup-button text-white hover:bg-gray-50 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">가입하기</button>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </body>
</template>






<style>

html {
  background-color: #E7EDF5;
  font-family: 'Noto Sans KR', sans-serif;
  height: 100%;
  width: 100%;
  padding: 0;
  margin: 0;
}

div.well {
  height: 250px;
}

input:focus {
  background-color: #E6F0FD;
  color: black;
}


.Absolute-Center {
  margin: auto;
  position: absolute;
  top: 0; left: 0; bottom: 0; right: 0;
  background-color: white;
}

.Absolute-Center.is-Responsive {
  width: 45%;
  height: 70%;
  min-width: 200px;
  max-width: 300px;
  padding: 40px 60px 40px 60px;
  border-radius: 12px;
}


#logo-container{
  font-size: 40px;
  color: #5A9FFE;
  border-radius: 10px;
  font-family: 'Righteous', sans-serif;
}

.login-input {
  margin-top: 8rem;
  margin-bottom: 3rem;
}

.button-selectId {
  display: flex;
  align-items: center;
}

.button-selectId input{

}

.login-middle {
  display: flex;
  justify-content: space-between;
  align-content: center;
  width: 100%;
  margin-top: 12rem;
}

.login-bottom {
  width: 100%;
}

.login-button {
  width: 100%;
  background: #5A9FFE;
}

.signup-button {
  width: 100%;
  background: white;
  border: 1px solid lightgray;
  color: rgb(128, 128, 128);
}

</style>