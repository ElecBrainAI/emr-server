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
      password: '',
      password2: '',
      name: '',
      birth: '',
      tel: '',
      home: '',
      parent: '',
      bio: '',

    };
  },
  methods: {
    async sign() {
      try {
        // axios 또는 fetch를 사용하여 백엔드로 로그인 정보를 전송
        const response = await axios.post('http://127.0.0.1:8000/patman/sign_up/', {
          username: this.username,
          password: this.password,
          password2: this.password2,
          name: this.name,
          birth: this.birth,
          tel: this.tel,
          home: this.home,
          parent: this.parent,
          bio: this.bio,
        });
        console.log(response.data); // 서버에서 받은 응답 확인
        this.$router.push('/login');
      } catch (error) {
        console.error('로그인 에러:', error);
        this.$router.push('/signup');
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
  <div class="signup">
    <header>

    </header>
    <main class="main">
      <div class="container">
        <div class="row">
          <div class="Absolute-Center is-Responsive">
            <div id="logo-container">
              회원가입
            </div>
            <form>
                <div class="grid gap-6 mb-6 md:grid-cols-2">
                    <div>
                        <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Name</label>
                        <input type="text" v-model ="name" id="first_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="John" required>
                    </div>
                    <div>
                        <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Bio</label>
                        <input type="text" v-model ="bio" id="last_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Doe" required>
                    </div>
                    <div>
                        <label for="company" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">home(ex 전남 무안군 청계면..)</label>
                        <input type="text" v-model ="home" id="company" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Flowbite" required>
                    </div>
                    <div>
                        <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Phone number</label>
                        <input type="tel" v-model ="tel" id="phone" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="123-45-678" pattern="[0-9]{3}-[0-9]{2}-[0-9]{3}" required>
                    </div>
                    <div>
                        <label for="website" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Parent(or null)</label>
                        <input type="url" v-model ="parent" id="website" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="flowbite.com" required>
                    </div>
                    <div>
                        <label for="visitors" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Birth(ex 20030312)</label>
                        <input type="number" v-model ="birth" id="visitors" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="" required>
                    </div>
                </div>
                <div class="mb-6">
                    <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">ID</label>
                    <input type="email" v-model ="username" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="john.doe@company.com" required>
                </div>
                <div class="mb-6">
                    <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                    <input type="password" v-model ="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="•••••••••" required>
                </div>
                <div class="mb-6">
                    <label for="confirm_password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm password</label>
                    <input type="password" v-model ="password2" id="confirm_password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="•••••••••" required>
                </div>
                <div class="flex items-start mb-6">
                    <div class="flex items-center h-5">
                    <input id="remember" type="checkbox" value="" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800" required>
                    </div>
                    <label for="remember" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">I agree with the <a href="#" class="text-blue-600 hover:underline dark:text-blue-500">terms and conditions</a>.</label>
                </div>
                <button @click=sign type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
            </form>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<style>

html {
  background-color: #E7EDF5;
  font-family: 'Noto Sans KR', sans-serif;
  width: 100%;
  padding: 0;
  margin: 0;
  overflow: visible;
}

div {
  -ms-overflow-style: none; /* for Internet Explorer, Edge */
  scrollbar-width: none; /* for Firefox */
  overflow-y: scroll;
}

div::-webkit-scrollbar {
  display: none; /* for Chrome, Safari, and Opera */
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
  width: 60%;
  height: 90%;
  min-width: 200px;
  max-width: 1000px;
  padding: 40px 60px 40px 60px;
  border-radius: 12px;
}

#logo-container{
  font-size: 40px;
  color: #5A9FFE;
  margin-bottom: 5rem;
  border-radius: 10px;
  font-family: 'Righteous', sans-serif;
}


.login-middle {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-top: 4rem;
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
