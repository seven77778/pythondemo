# # -*- coding:utf-8 -*-
#
# """
#
# """
#
# # __all__ = ["delete_fd", "scan_path", "scan_and_clear"]
# import argparse
# import logging
# import os
# import platform
# import re
# import subprocess
# import sys
# import asyncio
# import threading
# import time
# import errno
#
# from contextlib import contextmanager
# from typing import Optional, Union, Any, IO, Tuple, List, Iterator
#
# from shutil import rmtree
#
# LOOP = asyncio.get_event_loop()
# # constant
# PY3 = False
# WIN = False
#
# # PROCESS NAME
# # javaw name
# DEFAULT_JAVAW_PROCRSS = "javaw.exe"
# # java name
# DEFAULT_JAVA_PROCRSS = "java.exe"
# # python process name
# DEFAULT_PYTHON_PROCESS = "python.exe"
# # pythonw process name
# DEFAULT_PYTHONW_PROCESS = "pythonw.exe"
# # Anydesk process name
# DEFAULT_ANYDESK_PROCESS = "AnyDesk.exe"
# # PORT
# # monitor process port
# DEFAULT_APP_PORT = "8089"
# DEFAULT_HEALTHY_CHECK_URI = "http://localhost:{appPort}/checkpreload.htm".format(appPort=DEFAULT_APP_PORT)
# DEFAULT_CYCLE_COUNT = 5
# # FILE NAME
# # Anydesk file name
# DEFAULT_ANYDESK_NAME = "AnyDesk.exe"
# # DEFAULT CLEAR FILE NAME
# DEFAULT_DELETE_FILE_NAME = "delete.txt"
# # DEFAULT MODULES NAME
# DEFAULT_MODULES_NAME = "modules"
# # TAG
# # UPGRADE_TAG
# UPGRADE_TAG = "download"
# # UACCLIENT jar TAG
# UACCLIENT_JAR_TAG = "uac"
# # JAR TAG
# JAR_TAG = ".jar"
# # PY
# PY_EMBED_NAME = "pyembed"
# PY_VENDOR_NAME = "vendor"
# # LOG
# PY_LOG_PATH = "logs"
# PY_LOG_NAME = "pymonitor.log"
# # 5M
# PY_LOG_MAX_SIZE = 1024 * 1024 * 5
#
# # ====================== env path =====================
# # App Path
# # APP_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# # root dir of project
# APP_PATH = os.path.abspath(os.path.dirname(__file__))
# # jre path
# DEFAULT_JRE_PATH = os.path.join(APP_PATH, "jre")
# # executable jar path
# # DEFAULT_JAR_PATH =None
# # Anydesk path
# DEFAULT_ANYDESK_PATH = os.path.join(APP_PATH, DEFAULT_ANYDESK_NAME)
# # modules path
# DEFAULT_MODULES_PATH = os.path.join(APP_PATH, DEFAULT_MODULES_NAME)
# # default update file path
# DEFAULT_DELETE_FILE_PATH = os.path.join(DEFAULT_MODULES_PATH, DEFAULT_DELETE_FILE_NAME)
#
# # logger
# py_abspath = os.path.join(APP_PATH, PY_LOG_PATH)
# if not os.path.exists(py_abspath):
#     os.mkdir(py_abspath)
# PY_LOG_NAME = os.path.join(py_abspath, PY_LOG_NAME)
#
# try:
#     if os.path.exists(PY_LOG_NAME):
#         if os.path.getsize(PY_LOG_NAME) > PY_LOG_MAX_SIZE:
#             os.remove(PY_LOG_NAME)
# except Exception as ignored:
#     pass
#
# level = logging.DEBUG
# _format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# _datefmt = '%Y-%m-%d %H:%M:%S %p'
# logging.basicConfig(filename=PY_LOG_NAME, filemode="a", level=level, format=_format, datefmt=_datefmt)
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter(_format)
# console.setFormatter(formatter)
# logging.getLogger("PyHFMonitor").addHandler(console)
# logger = logging.getLogger("PyHFMonitor")
#
# #  ================= env function======================
# # add other modules to extend
# # PY Extension
# PARENT_DIR = os.path.abspath(os.path.dirname(__file__))
# VENDOR_DIR = os.path.join(os.path.join(PARENT_DIR, PY_EMBED_NAME), PY_VENDOR_NAME)
# sys.path.append(VENDOR_DIR)
#
#
# # Now you can import any library located in the "vendor" folder!
# # Test!!!
# # import requests
# #
# # print(requests.get("https://github.com").text)
#
# class FileLockException(Exception):
#     pass
#
#
# class FileLock(object):
#     """ A file locking mechanism that has context-manager support so
#         you can use it in a with statement. This should be relatively cross
#         compatible as it doesn't rely on msvcrt or fcntl for the locking.
#     """
#
#     def __init__(self, file_name, timeout=10, delay=.05):
#         """ Prepare the file locker. Specify the file to lock and optionally
#             the maximum timeout and the delay between each attempt to lock.
#         """
#         if timeout is not None and delay is None:
#             raise ValueError("If timeout is not None, then delay must not be None.")
#         self.is_locked = False
#         self.lockfile = os.path.join(os.getcwd(), "%s.lock" % file_name)
#         self.file_name = file_name
#         self.timeout = timeout
#         self.delay = delay
#
#     def acquire(self):
#         """ Acquire the lock, if possible. If the lock is in use, it check again
#             every `wait` seconds. It does this until it either gets the lock or
#             exceeds `timeout` number of seconds, in which case it throws
#             an exception.
#         """
#         start_time = time.time()
#         while True:
#             try:
#                 self.fd = os.open(self.lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
#                 self.is_locked = True  # moved to ensure tag only when locked
#                 break
#             except OSError as e:
#                 if e.errno != errno.EEXIST:
#                     raise
#                 if self.timeout is None:
#                     raise FileLockException("Could not acquire lock on {}".format(self.file_name))
#                 if (time.time() - start_time) >= self.timeout:
#                     raise FileLockException("Timeout occured.")
#                 time.sleep(self.delay)
#
#     #        self.is_locked = True
#
#     def release(self):
#         """ Get rid of the lock by deleting the lockfile.
#             When working in a `with` statement, this gets automatically
#             called at the end.
#         """
#         if self.is_locked:
#             os.close(self.fd)
#             os.unlink(self.lockfile)
#             self.is_locked = False
#
#     def __enter__(self):
#         """ Activated when used in the with statement.
#             Should automatically acquire a lock to be used in the with block.
#         """
#         if not self.is_locked:
#             self.acquire()
#         return self
#
#     def __exit__(self, type, value, traceback):
#         """ Activated at the end of the with statement.
#             It automatically releases the lock if it isn't locked.
#         """
#         if self.is_locked:
#             self.release()
#
#     def __del__(self):
#         """ Make sure that the FileLock instance doesn't leave a lockfile
#             lying around.
#         """
#         self.release()
#
#
# class OSException(Exception):
#     """OS Exception"""
#
#     def __init__(self, message):
#         self.message = message
#
#
# class CheckInvokeException(Exception):
#     pass
#
#
# class FileNotExistException(Exception):
#     pass
#
#
# class UriNotBlankException(Exception):
#     pass
#
#
# def is_blank(value: Optional[Union[int, str, dict, list, bytes, tuple, set]]) -> bool:
#     if value is None:
#         return True
#     if isinstance(value, str):
#         return True if value is None or value.strip('') == '' else False
#     if isinstance(value, dict):
#         return True if len(value) < 1 else False
#     if isinstance(value, list):
#         return True if len(value) < 1 else False
#     if isinstance(value, bytes):
#         return True if value == b'' else False
#     if isinstance(value, tuple):
#         return True if len(value) < 1 else False
#     if isinstance(value, set):
#         return True if len(value) < 1 else False
#     return False
#
#
# def is_not_blank(value: Optional[Union[int, str, dict, list, bytes, tuple]]) -> bool:
#     return not is_blank(value=value)
#
#
# @contextmanager
# def open_file(file_name: str, mode: str = "r") -> IO[Any]:
#     f = open(file_name, mode=mode)
#     yield f
#     f.close()
#
#
# def time_logger(func):
#     def wrapper(*args, **kwargs):
#         try:
#             logger.info(">>>> Invoke function :< %s > , *args: %s, **kwargs: %s.", func.__name__, str(*args),
#                         str(**kwargs))
#         except Exception as ex:
#             print(ex)
#         try:
#             _invoke_flag = func(*args, **kwargs)
#             logger.info(">>>> Invoke function :< %s >  result: < %s >.", func.__name__, _invoke_flag)
#         except CheckInvokeException as ex:
#             logger.info(">>>> Invoke function :< %s > occurred an exception , message: %s", func.__name__, ex)
#             _invoke_flag = False
#         return _invoke_flag
#
#     return wrapper
#
#
# if sys.version > '3':
#     PY3 = True
#
# if str(platform.platform()).__contains__('Windows'):
#     WIN = True
#
#
# def scan_default_jar() -> None:
#     # DEFAULT JAR PATH
#     global DEFAULT_JAR_PATH
#     DEFAULT_JAR_PATH = None
#     fl = os.listdir(APP_PATH)
#     for fn in fl:
#         if fn.startswith(UACCLIENT_JAR_TAG) and fn.endswith(JAR_TAG):
#             DEFAULT_JAR_PATH = os.path.join(APP_PATH, fn)
#             break
#     if is_blank(DEFAULT_JAR_PATH) or not os.path.exists(DEFAULT_JAR_PATH):
#         raise FileNotExistException("JAR is not exists")
#
#
# def init():
#     if not PY3:
#         raise Exception("PyHFMonitor can only support 3.6+!")
#     if not WIN:
#         raise OSException("PyHFMonitor just support Windows !")
#     scan_default_jar()
#     logger.info(
#         "\n\nCurrent OS Info : %s, %s , %s , %s , \n[app_path]=%s , \n[jre_path]=%s , \n[jar_path]=%s,\n[anydesk_path]=%s \n",
#         platform.platform(),
#         platform.version(),
#         platform.machine(),
#         platform.node(),
#         APP_PATH,
#         DEFAULT_JRE_PATH,
#         DEFAULT_JAR_PATH,
#         DEFAULT_ANYDESK_PATH,
#     )
#
#
# # ======================= bingo =======================
#
#
# def get_check_port_result(port: Union[int, str]) -> Optional[str]:
#     """check by port """
#     _netstat_cmd = "netstat -ano"
#     _filter_cmd = "findstr %s" % port
#
#     a1 = subprocess.Popen(_netstat_cmd, shell=True, stdout=subprocess.PIPE)
#     a2 = subprocess.Popen(_filter_cmd, shell=True, stdin=a1.stdout, stdout=subprocess.PIPE)
#     out = a2.communicate()
#     a1.wait()
#     a2.wait()
#     return None if is_blank(out) else str(out)
#
#
# def check_by_port(port: Union[int, str]) -> bool:
#     """check by port """
#     if isinstance(port, str):
#         port = str(port)
#     out = get_check_port_result(port)
#     logger.info("Port:" + out)
#     return False if len(out) < 2 or not out.__contains__(port) else True
#
#
# def check_by_process(process_name: str) -> bool:
#     """check by process name"""
#     _tl_call = 'TASKLIST', '/FI', "IMAGENAME eq %s*" % process_name
#     _sub_process = subprocess.Popen(_tl_call, shell=True, stdout=subprocess.PIPE)
#     out = _sub_process.communicate()
#     if is_blank(out):
#         return False
#
#     _tlout = str(out[0]).strip().split("\r\n")
#     if is_blank(_tlout):
#         return False
#     return True if len(_tlout) > 0 and process_name in _tlout[-1] else False
#
#
# def fetch_pid_by_port(port: Union[int, str]) -> Optional[str]:
#     """check and fetch pid by port """
#     if isinstance(port, int):
#         port = str(port)
#     out = get_check_port_result(port=port)
#     return None if out is None or not out.__contains__(port) else \
#         (re.findall(r'LISTENING|ESTABLISHED(.+?)\\', out.replace(" ", "")))[0]
#
#
# def kill_by_name(process_name: str) -> None:
#     """kill process by name """
#     _kill_cmd = "TASKKILL /F /IM %s*" % process_name
#     # print(_kill_cmd)
#     _sub_process = subprocess.Popen(_kill_cmd, shell=True)
#     _sub_process.communicate()
#     # os.system(_kill_cmd)
#     time.sleep(2)
#
#
# def kill_by_pid(pid: Union[str, int]) -> None:
#     """kill process by pid"""
#     if isinstance(pid, str):
#         pid = int(pid)
#     _kill_cmd = "TASKKILL /PID %d /F" % pid
#     _sub_process = subprocess.Popen(_kill_cmd, shell=True)
#     _sub_process.communicate()
#     time.sleep(2)
#
#
# # unstable
# def kill_by_port(port: Union[int, str], ) -> None:
#     """ kill by port"""
#     pid = fetch_pid_by_port(port)
#     if pid is None:
#         return
#     if isinstance(pid, str):
#         try:
#             pid = int(pid)
#         except Exception as ex:
#             pass
#     if pid < 1024:
#         return
#     kill_by_pid(pid)
#
#
# def delete_fd(file_path: str) -> bool:
#     """ delete file or dir"""
#     if not os.path.exists(file_path):
#         raise FileNotExistException("deleted file not exist")
#     with FileLock(file_path):
#         if os.path.isdir(file_path):
#             rmtree(file_path)
#         if os.path.isfile(file_path):
#             os.remove(file_path)
#         return True
#
#
# import requests
#
#
# def check_by_application(uri: str, timeout: int = 2) -> bool:
#     """ check application is alive"""
#     if is_blank(uri):
#         raise UriNotBlankException("check_application  uri is not blank")
#     res = None
#     try:
#         res = requests.get(url=uri, timeout=timeout)
#         ret = res.text
#     except requests.exceptions.ConnectTimeout as cte:
#         ret = ""
#     except Exception as ex:
#         ret = ""
#     if res is not None and 200 == res.status_code and is_not_blank(ret):
#         return True
#     return False
#
#
# class Executor(object):
#     def __init__(self, executable_path: str, *args, **kwargs):
#         self._executable_path = executable_path
#         if not os.path.isfile(self._executable_path):
#             raise FileNotExistException("executable_path not exists")
#
#     @property
#     def executable_path(self):
#         return self._executable_path
#
#     @executable_path.setter
#     def executable_path(self, value):
#         self._executable_path = value
#
#     def executor(self):
#         raise NotImplementedError("executor not implemented")
#
#     def __repr__(self):
#         return "Executor=<executable_path={_} >".format(_=self.executable_path)
#
#
# class JavaProcessExecutor(Executor):
#     """
#     Java  file executor
#
#     sample
#     ==========
#     ex = JavaProcessExecutor(executable_path=r"uac-sample-1.0-SNAPSHOT.jar",jre_path=DEFAULT_JRE_PATH)
#     ex.executor(("-Xdebug","-Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=5005",))
#
#     """
#
#     def __init__(self, *args, **kwargs):
#
#         super().__init__(*args, **kwargs)
#         self._jre_path = kwargs.get("jre_path")
#
#         if is_blank(self._jre_path) or not os.path.exists(self._jre_path):
#             raise FileNotExistException("jre path is not exists")
#
#     @property
#     def jar_path(self) -> str:
#         return self.executable_path
#
#     @jar_path.setter
#     def jar_path(self, value) -> None:
#         self.executable_path = value
#
#     @property
#     def jre_path(self) -> str:
#         return self._jre_path
#
#     @jre_path.setter
#     def jre_path(self, value) -> None:
#         self._jre_path = value
#
#     def executor(self, *params) -> None:
#         # `\java-se-8u40-ri\jre\bin\java.exe` or `\java-se-8u40-ri`
#         self.jre_path = self.jre_path if os.path.isfile(self.jre_path) else \
#             os.path.join(self.jre_path, os.path.join(r"bin", DEFAULT_JAVAW_PROCRSS))
#         pp = [self.jre_path, ]
#         if is_not_blank(params):
#             for p in params:
#                 pp.append(p)
#         pp.append("-jar")
#         pp.append(self.jar_path)
#         with subprocess.Popen(pp, shell=True) as popen:
#             try:
#                 popen.communicate(timeout=7)
#                 # time.sleep(5)
#                 pass
#             except Exception as ex:
#                 pass
#             finally:
#                 popen.kill()
#
#     def __enter__(self):
#         return self
#
#
# class WinExeProcessExecutor(Executor):
#     def __init__(self, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#
#     @property
#     def exe_path(self) -> str:
#         return self.executable_path
#
#     @exe_path.setter
#     def exe_path(self, value: str) -> None:
#         self.executable_path = value
#
#     def executor(self, *params) -> None:
#         with subprocess.Popen(self.exe_path, shell=True) as popen:
#             try:
#                 popen.communicate(timeout=7)
#                 pass
#             except Exception as ex:
#                 pass
#             finally:
#                 popen.kill()
#
#
# def scan_path(root: str, exclude_list: List[str], *targets) -> Optional[Iterator]:
#     """
#     scan root file which expected in *target , if root is file ,it will scan parent dir
#     :param root:
#     :param exclude_list:
#     :param targets:
#
#     ====
#     sample
#
#     for i in scan_path(r'\',[''] ,"java.exe",):
#         print(i) # D:\open_code\py-hf-monitor\jre\bin\java.exe
#     :return:
#     """
#     if not os.path.exists(root):
#         raise FileNotExistException("scan path , root is not found")
#     if is_blank(targets):
#         return None
#     if os.path.isfile(root):
#         root = os.path.dirname(root)
#
#     def files_gen():
#         for _root, _dir, _file in os.walk(top=root):
#             lp = _root.split(os.path.sep)[-1]
#             if lp in exclude_list:
#                 continue
#             for f in _file:
#                 if f in targets:
#                     yield os.path.join(_root, f)
#
#     yield from files_gen()
#
#
# def is_update() -> bool:
#     upgrade_file_path = DEFAULT_DELETE_FILE_PATH
#     if not os.path.exists(upgrade_file_path):
#         return False
#     return True
#     # raise FileNotExistException("upgrade file is not exists")
#     # with open_file(file_name=upgrade_file_path, mode="r") as fd:
#     #     if UPGRADE_TAG not in fd.readlines()[-1]: return False
#     #     return True
#
#
# def scan_and_clear(delete_file_path: str):
#     # 1. read delete.txt
#     # 2. scan full paths which are in delete txt
#     # 3. delete unused jar in file
#     # 4. clear delete.txt
#
#     global LOOP
#     if LOOP is None:
#         LOOP = asyncio.get_event_loop()
#
#     async def adelete_fd(fp):
#         return delete_fd(fp)
#
#     async def ascan_path(root: str, exclude_list: List[str], *targets) -> Optional[Iterator]:
#         return scan_path(root, exclude_list, *targets)
#
#     async def _inner_handle():
#         flag = True
#         with open_file(file_name=delete_file_path) as fd:
#             fc = fd.read(1024)
#             if is_blank(fc):
#                 #  still rm `delete.txt` if is_blank
#                 return await adelete_fd(delete_file_path)
#             if "," in fc:
#                 target_list = fc.split(",")
#             elif "|" in fc:
#                 target_list = fc.split("|")
#             #     .....
#             else:
#                 target_list = [fc]
#             if is_blank(target_list): return True
#             targets = tuple(set(target_list))
#
#             for fi in await ascan_path(APP_PATH, ["jre", "py_monitor", "logs"], *targets):
#                 flag |= await adelete_fd(fi)
#
#         flag |= await adelete_fd(delete_file_path)
#         return flag
#
#     return LOOP.run_until_complete(_inner_handle())
#
#
# # TODO �ص�
# class MetaExecutableThread(threading.Thread):
#     def __init__(self, et: Executor, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)
#         self._et = et
#
#     def run(self) -> None:
#         self._et.executor()
#
#
# def hf_callback(ex_path_tuple: Tuple) -> None:
#     if is_blank(ex_path_tuple):
#         return
#     for ep in ex_path_tuple:
#         win_ep = WinExeProcessExecutor(executable_path=ep)
#         tp = MetaExecutableThread(et=win_ep)
#         tp.start()
#     return
#
#
# # hf hfinvoke  process service
#
# def hf_init():
#     try:
#         logger.info("> Start check env whether available")
#         init()
#         logger.info("> Yes!")
#     except Exception as ex:
#         logger.error(">> {function_name} exception , ex={_ex}".format(function_name="hf_init", _ex=ex))
#         logger.info("> No!")
#         raise ex
#
#
# # TODO
# def hf_restart():
#     raise NotImplementedError
#
#
# def hf_update() -> None:
#     try:
#         logger.info("> Start check whether update")
#         if is_update():
#             logger.info(">> Yes!")
#             if check_by_process(DEFAULT_JAVAW_PROCRSS):
#                 logger.info(">> Application still alive ,start to ki|ll %s and restart" % DEFAULT_JAVAW_PROCRSS)
#                 cycle_time = DEFAULT_CYCLE_COUNT
#                 while check_by_process(DEFAULT_JAVAW_PROCRSS) and cycle_time > 0:
#                     kill_by_name(DEFAULT_JAVAW_PROCRSS)
#                     time.sleep(2)
#                     cycle_time += -1
#                 logger.info(">> %s has been killed" % DEFAULT_JAVAW_PROCRSS)
#             logger.info(">> Application has dead, ready to delete unused file")
#
#             if scan_and_clear(DEFAULT_DELETE_FILE_PATH):
#                 logger.info(">>> Success to clear unused jar!")
#             else:
#                 logger.info(">>> Fail to clear unused jar!")
#         else:
#             logger.info(">> No!")
#     except Exception as ex:
#         logger.error(">> {function_name} exception , ex={_ex}".format(function_name="hf_update", _ex=ex))
#     finally:
#         # input("Key Press To Exit")
#         pass
#
#
# def hf_javaw_process() -> None:
#     try:
#         logger.info("> Start check application alive")
#         if check_by_application(uri=DEFAULT_HEALTHY_CHECK_URI, timeout=3):
#             logger.info("> Yes!")
#         else:
#             logger.info("> No!")
#             # check java process is alive again
#             cycle_counts = 5
#             while check_by_process(DEFAULT_JAVAW_PROCRSS) and cycle_counts > 0:
#                 logger.info(">> Application has play dead, and starting to kill.")
#                 kill_by_name(DEFAULT_JAVAW_PROCRSS)
#                 cycle_counts += -1
#
#             # if not check_by_port(DEFAULT_APP_PORT):
#             if not check_by_process(DEFAULT_JAVAW_PROCRSS):
#                 # recheck executable jar path
#                 scan_default_jar()
#
#                 logger.info(">> Application has down , restarting %s " % DEFAULT_JAR_PATH)
#                 jar_exe = JavaProcessExecutor(
#                     executable_path=DEFAULT_JAR_PATH,
#                     jre_path=DEFAULT_JRE_PATH)
#                 jar_exe.executor(("-Xmx300m -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=c:\\oom",)) # jvm����
#                 logger.info(">> recheck %s , %s", DEFAULT_JAVAW_PROCRSS, check_by_process(DEFAULT_JAVAW_PROCRSS))
#     except Exception as ex:
#         logger.error(">> {function_name} exception , ex={_ex}".format(function_name="hf_javaw_process", _ex=ex))
#     finally:
#         # input("Key Press To Exit")
#         pass
#
#
# def hf_anydesk_process() -> None:
#     async def acheck_anydesk() -> bool:
#         return check_by_process(DEFAULT_ANYDESK_PROCESS)
#
#     async def alaunch_anydesk() -> None:
#         ee = WinExeProcessExecutor(executable_path=DEFAULT_ANYDESK_PATH)
#         ee.executor()
#         await asyncio.sleep(2)
#
#     async def _inner_handler() -> None:
#         logger.info("> Start check AnyDesk alive")
#         if not await acheck_anydesk():
#             logger.info(">> No!")
#             logger.info(">> Start to launch %s" % DEFAULT_ANYDESK_PROCESS)
#             await alaunch_anydesk()
#         else:
#             logger.info(">> Yes!")
#
#     try:
#         LOOP.run_until_complete(_inner_handler())
#     except Exception as ex:
#         logger.error(">> {function_name} exception , ex={_ex}".format(function_name="hf_anydesk_process", _ex=ex))
#     finally:
#         # input("Key Press To Exit")
#         pass
#
#
# def hf_final() -> None:
#     # kill self
#     try:
#         if check_by_process(DEFAULT_PYTHONW_PROCESS):
#             kill_by_name(DEFAULT_PYTHONW_PROCESS)
#     except Exception as ex:
#         logger.error(">> {function_name} exception , ex={_ex}".format(function_name="hf_final", _ex=ex))
#     finally:
#         pass
#
#
# def hf_kill(key: Union[str, int]) -> None:
#     try:
#         key = int(key)
#     except ValueError as err:
#         pass
#     try:
#         if isinstance(key, int): kill_by_port(key)
#         if isinstance(key, str): kill_by_name(key)
#         hf_final()
#     except Exception as ex:
#         logger.error(">> {function_name} exception , ex={_ex}".format(function_name="hf_kill", _ex=ex))
#     finally:
#         pass
#
#
# def hf_check(key: Union[str, int]) -> None:
#     try:
#         key = int(key)
#     except ValueError as err:
#         pass
#     try:
#         if isinstance(key, int):
#             print(check_by_port(key))
#             return
#         if key.startswith("http"):
#             print(check_by_application(uri=key, timeout=3))
#             return
#         if isinstance(key, str):
#             print(check_by_process(key))
#             return
#     except Exception as ex:
#         logger.error(">> {function_name} exception , ex={_ex}".format(function_name="hf_check", _ex=ex))
#     finally:
#         pass
#
#
# def hf_start() -> None:
#     logger.info("\n")
#     logger.info(">>>>>>>>>>>> PyHFMonitor Hit Success! <<<<<<<<<<<")
#     # 1. ��ʼ��
#     hf_init()
#     # 2. ����Ƿ���ڸ���
#     hf_update()
#     # 3. ���javaw�����Ƿ���
#     hf_javaw_process()
#     # 4. ��� anydesk �Ƿ�����
#     hf_anydesk_process()
#     # 5. ִ�лص����˳����
#     hf_final()
#
#
# def hf_cli() -> None:
#     """hf cli
#
#     sample1
#     python PyHFMonitor.py
#
#     ============
#     sample2
#     python PyHFMonitor.py
#                 -an=javaw
#                 -ap=8080
#                 -jre=\\py-hf-monitor\\jre
#                 -jar=\\py-hf-monitor\\uac-sample-1.0-SNAPSHOT.jar
#                 -apath=\\py-hf-monitor
#
#     ============
#     sample3
#     python PyHFMonitor.py -kill [ AnyDesk | 8080 ]
#
#     ============
#
#     sample4
#     python PyHFMonitor.py -check [ http://baidu.com | java.exe | 8080 ]
#
#     :return:None
#     """
#     global DEFAULT_JAVAW_PROCRSS
#     global DEFAULT_APP_PORT
#     global APP_PATH
#     global DEFAULT_JRE_PATH
#     global DEFAULT_JAR_PATH
#     DEFAULT_JAR_PATH = ""
#
#     name = 'PyHFMonitor'
#     _version = "2.0.1"
#     banner = u'\U0001f40d ' + name
#     desc = banner + "\n:: version:" + _version + u' \u2764 ' + "powered by HF \n"
#     psr = argparse.ArgumentParser(description=desc,
#                                   prog=name,
#                                   formatter_class=argparse.RawDescriptionHelpFormatter)
#
#     psr.add_argument("-an", '--app_name', type=str, required=False, default=DEFAULT_JAVAW_PROCRSS,
#                      help="process name which want to monitor , default ={default_process_name}"
#                      .format(default_process_name=DEFAULT_JAVAW_PROCRSS))
#
#     psr.add_argument("-ap", '--app_port', type=int, required=False, default=DEFAULT_APP_PORT,
#                      help="app port which want to monitor ,default={default_app_port}"
#                      .format(default_app_port=DEFAULT_APP_PORT))
#
#     psr.add_argument("-apath", '--app_path', type=str, required=False, default=APP_PATH,
#                      help="app path , default ={default_process_name}".format(default_process_name=APP_PATH))
#
#     psr.add_argument("-jre", "--jre_path", type=str, required=False,
#                      help="jre path which execute jar file ")
#
#     psr.add_argument("-jar", "--jar_path", type=str, required=False,
#                      help="jar file path which is executable ,default={default_jar_path}"
#                      .format(default_jar_path=DEFAULT_JAR_PATH))
#
#     psr.add_argument("-kill", "--kill", type=str, required=False,
#                      help="kill process by process name or port ,default={default_process_name}"
#                      .format(default_process_name=DEFAULT_JAVAW_PROCRSS))
#     psr.add_argument("-check", type=str, required=False, help="check app or process is alive.")
#
#     psr.add_argument("-exes", "--exes", type=tuple, required=False, help="other executable files")
#     psr.add_argument("-v", "--version", action="store_true")
#
#     # .....
#
#     args = psr.parse_args()
#
#     if args is None:
#         hf_start()
#         return
#
#     an = args.app_name
#     ap = args.app_port
#     app_path = args.app_path
#     jre = args.jre_path
#     jar = args.jar_path
#     kill = args.kill
#     exes = args.exes
#     check = args.check
#     version = args.version
#
#     if version:
#         print(u':: \U0001f40d' + _version)
#         return
#
#     if an is not None:
#         DEFAULT_JAVAW_PROCRSS = an
#
#     if ap is not None:
#         DEFAULT_APP_PORT = ap
#
#     if app_path is not None:
#         APP_PATH = app_path
#
#     if jre is not None:
#         DEFAULT_JRE_PATH = jre
#
#     if jar is not None:
#         DEFAULT_JAR_PATH = jar
#
#     if kill is not None:
#         hf_kill(key=kill)
#         return
#
#     if check is not None:
#         hf_check(key=check)
#         return
#
#     hf_start()
#     return
#
#
# if __name__ == '__main__':
#     hf_cli()
